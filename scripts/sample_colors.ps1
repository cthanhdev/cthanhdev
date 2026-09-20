Add-Type -AssemblyName System.Drawing
$imgFile = (Resolve-Path "assets\hero.jpg").Path
$bmp = [System.Drawing.Bitmap]::FromFile($imgFile)

$p1 = $bmp.GetPixel(50, 480)
$p2 = $bmp.GetPixel(180, 250)
$p3 = $bmp.GetPixel(580, 480)
$p4 = $bmp.GetPixel(300, 300)
$p5 = $bmp.GetPixel(620, 180)
$p6 = $bmp.GetPixel(500, 40)
$p7 = $bmp.GetPixel(850, 45)

$bmp.Dispose()

Write-Output ("Dark Foreground Frame (Dark Slate Black) : #{0:x2}{1:x2}{2:x2}" -f $p1.R, $p1.G, $p1.B)
Write-Output ("Window Pillar (Steel Slate)              : #{0:x2}{1:x2}{2:x2}" -f $p2.R, $p2.G, $p2.B)
Write-Output ("Rei Uniform (Navy Shadow Slate)          : #{0:x2}{1:x2}{2:x2}" -f $p3.R, $p3.G, $p3.B)
Write-Output ("Skyscraper Midtone (Concrete Mist)       : #{0:x2}{1:x2}{2:x2}" -f $p4.R, $p4.G, $p4.B)
Write-Output ("Rei Hair / Reflection (Ice Blue Mist)    : #{0:x2}{1:x2}{2:x2}" -f $p5.R, $p5.G, $p5.B)
Write-Output ("Sky Haze (Atmospheric Silver White)      : #{0:x2}{1:x2}{2:x2}" -f $p6.R, $p6.G, $p6.B)
Write-Output ("Evangelion LCL Horizon (Subtle Crimson)  : #{0:x2}{1:x2}{2:x2}" -f $p7.R, $p7.G, $p7.B)
