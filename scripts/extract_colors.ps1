Add-Type -AssemblyName System.Drawing
$imgFile = (Resolve-Path "assets\hero.jpg").Path
$bmp = [System.Drawing.Bitmap]::FromFile($imgFile)
$w = $bmp.Width
$h = $bmp.Height

$samples = @()
for ($y = 0; $y -lt $h; $y += 15) {
    for ($x = 0; $x -lt $w; $x += 15) {
        $p = $bmp.GetPixel($x, $y)
        # Quantize to group nearby colors (round to nearest 16)
        $r = [Math]::Round($p.R / 16) * 16
        $g = [Math]::Round($p.G / 16) * 16
        $b = [Math]::Round($p.B / 16) * 16
        if ($r -gt 255) { $r = 255 }
        if ($g -gt 255) { $g = 255 }
        if ($b -gt 255) { $b = 255 }
        $samples += ("#{0:X2}{1:X2}{2:X2}" -f [int]$r, [int]$g, [int]$b)
    }
}
$bmp.Dispose()

Write-Output "--- DOMINANT COLOR PALETTE ---"
$samples | Group-Object | Sort-Object Count -Descending | Select-Object -First 20 | ForEach-Object {
    Write-Output ("{0} : {1}" -f $_.Name, $_.Count)
}
