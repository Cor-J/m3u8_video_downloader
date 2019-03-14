param([String]$Url,[String]$Path)

#function DownloadTsFiles([string[]]$list_name,[string]$url,[string]$path_parent)
$task_DownloadTsFiles = {
    param($list_name,$url,$path_parent)
    #$sum = [double]$list_name.Count
    #$count = [double]0
    $last_file = "null"
    $last_url = "null"
    #write-progress -Activity "Downloading ts files" -Status "$count/$sum Completed" -PercentComplete 0 -Id 1
    foreach ($name in $list_name)
    {
        #$per = [int]($count * 100.0 / $sum)
        $tmp_url = $url + "/" + $name
        $tmp_path = $path_parent + "\tmpTsFiles\" + $name
        #$progressPreference = 'silentlyContinue'
        if(!(Test-Path($tmp_path)))
        {
            Invoke-WebRequest -uri $tmp_url -OutFile $tmp_path -UseBasicParsing
            if(Test-Path($last_file))
            {
                Invoke-WebRequest -uri $last_url -OutFile $last_file -UseBasicParsing
                $last_file = "null"
                $last_url = "null"
            }
        } else {
            $last_file = $tmp_path
            $last_url = $tmp_url
        }
        #$progressPreference = 'Continue'
        #$count = $count + 1
        #write-progress -Activity "Downloading ts files" -Status "$count/$sum Completed" -PercentComplete $per -Id 1
    }
    Unblock-File $path_parent
}

#function MergingTsFiles([string[]]$list_path,[string]$path)
$task_MergingTsFiles = {
    param($list_path,$path)
    $sum = [double]$list_path.Count
    $count = [double]0
    write-progress -Activity "Merging ts files" -Status "$count/$sum Completed" -PercentComplete 0 -Id 2
    foreach ($file in $list_path)
    {
        $per = [int]($count * 100.0 / $sum)
        $per_download = [int]($count_download * 100.0 / $sum)
        while(1)
        {
            try {
                $ByteArray = [System.IO.File]::ReadAllBytes($file)
                ##$ByteArray = Get-Content -Encoding Byte -Path $file -Raw
                Add-Content -Encoding Byte -Path $path -Value $ByteArray
            }
            catch {
                write-progress -Activity "Merging ts files" -Status "$count/$sum Completed. Waiting for downloading ts files" -PercentComplete $per -Id 2
                Start-Sleep -Seconds 1
                continue
            }
            break
        }
        $count = $count + 1
        write-progress -Activity "Merging ts files" -Status "$count/$sum Completed" -PercentComplete $per -Id 2
    }
}

$url_m3u8 = $Url
$name_m3u8 = Split-Path -Leaf $url_m3u8
$url = $url_m3u8.Replace("/"+$name_m3u8,"")
$source_path = $Path
$path = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($Path)
$path_parent = Split-Path -Parent $path
$path_m3u8 = $path_parent + "\" + $name_m3u8
if(Test-Path $path){
    del $path -recurse
}
if(!(Test-Path($path_parent))){
    $null = New-Item -Path $path_parent -Type Directory -Force
}

echo "Downloading m3u8 file..."
$progressPreference = 'silentlyContinue'
Invoke-WebRequest -uri $url_m3u8 -OutFile $path_m3u8 -UseBasicParsing
$progressPreference = 'Continue'
Unblock-File $path_m3u8
echo "...done"

echo "Loading m3u8 file..."
$content = Get-Content -Path $path_m3u8 -Raw
$list_name = $content | findstr.exe ".ts"
$list_path = $list_name | foreach{$path_parent + "\tmpTsFiles\" + $_}
echo "...done"

echo "Creating tmp directory..."
$tmp_ts_path = $path_parent + "\tmpTsFiles"
if(!(Test-Path ($tmp_ts_path))){
    $null = New-Item -Type Directory -Path $tmp_ts_path
}
echo "...done"
 
echo "Downloading and merging ts files..."
$job1 =  Start-Job -ArgumentList $list_name,$url,$path_parent -ScriptBlock $task_DownloadTsFiles
$job2 =  Invoke-Command -ArgumentList $list_path,$path -ScriptBlock $task_MergingTsFiles
$nulls = Wait-Job -Job $job1
Remove-Job -Job $job1
echo "...done"

echo "Deleting ts files..."
del $tmp_ts_path -recurse
echo "...done"

echo "Deleting m3u8 file..."
del $path_m3u8 -recurse
echo "...done"
