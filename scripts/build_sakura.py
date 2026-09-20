import os

os.makedirs('assets', exist_ok=True)

# 1. Generate assets/sakura_banner.svg
banner_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="100%" preserveAspectRatio="xMidYMid slice">
  <defs>
    <!-- Sky Gradient: Midnight Violet to Deep Sakura Twilight -->
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0514" />
      <stop offset="35%" stop-color="#160c26" />
      <stop offset="70%" stop-color="#241036" />
      <stop offset="100%" stop-color="#0e0719" />
    </linearGradient>

    <!-- Sakura Mist Glows -->
    <radialGradient id="mist1" cx="25%" cy="35%" r="50%">
      <stop offset="0%" stop-color="#f472b6" stop-opacity="0.18" />
      <stop offset="60%" stop-color="#a855f7" stop-opacity="0.05" />
      <stop offset="100%" stop-color="#0a0514" stop-opacity="0" />
    </radialGradient>
    <radialGradient id="mist2" cx="80%" cy="60%" r="45%">
      <stop offset="0%" stop-color="#fb7185" stop-opacity="0.16" />
      <stop offset="50%" stop-color="#c084fc" stop-opacity="0.06" />
      <stop offset="100%" stop-color="#0a0514" stop-opacity="0" />
    </radialGradient>

    <!-- Text Glow Filter -->
    <filter id="sakuraGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="5" result="blur" />
      <feFlood flood-color="#ff7597" flood-opacity="0.65" result="flood" />
      <feComposite in="flood" in2="blur" operator="in" result="glow" />
      <feMerge>
        <feMergeNode in="glow" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <!-- Pixel Petal Type 1 (Single Fluttering Petal) -->
    <g id="pixelPetal1">
      <rect x="3" y="0" width="3" height="3" fill="#ffd1dc" />
      <rect x="6" y="0" width="3" height="3" fill="#ff9ebb" />
      <rect x="0" y="3" width="3" height="3" fill="#ffb7c5" />
      <rect x="3" y="3" width="6" height="6" fill="#ff7597" />
      <rect x="9" y="3" width="3" height="3" fill="#f43f5e" />
      <rect x="3" y="9" width="3" height="3" fill="#ff7597" />
      <rect x="6" y="9" width="3" height="3" fill="#e11d48" />
    </g>

    <!-- Pixel Petal Type 2 (Tilted Petal) -->
    <g id="pixelPetal2">
      <rect x="3" y="0" width="3" height="3" fill="#ffe4e6" />
      <rect x="0" y="3" width="3" height="3" fill="#fecdd3" />
      <rect x="3" y="3" width="6" height="6" fill="#fda4af" />
      <rect x="6" y="6" width="3" height="3" fill="#fb7185" />
      <rect x="3" y="6" width="3" height="3" fill="#f43f5e" />
    </g>

    <!-- Pixel Flower (Full 5-Petal Blossom) -->
    <g id="pixelBlossom">
      <rect x="8" y="8" width="4" height="4" fill="#fef08a" />
      <rect x="8" y="2" width="4" height="4" fill="#ff9ebb" />
      <rect x="6" y="4" width="2" height="2" fill="#ffd1dc" />
      <rect x="12" y="4" width="2" height="2" fill="#ff7597" />
      <rect x="8" y="14" width="4" height="4" fill="#ff7597" />
      <rect x="6" y="14" width="2" height="2" fill="#fda4af" />
      <rect x="12" y="14" width="2" height="2" fill="#f43f5e" />
      <rect x="2" y="8" width="4" height="4" fill="#ffd1dc" />
      <rect x="4" y="6" width="2" height="2" fill="#ffe4e6" />
      <rect x="4" y="12" width="2" height="2" fill="#ff9ebb" />
      <rect x="14" y="8" width="4" height="4" fill="#ff7597" />
      <rect x="14" y="6" width="2" height="2" fill="#fda4af" />
      <rect x="14" y="12" width="2" height="2" fill="#f43f5e" />
    </g>

    <!-- Pixel Star (Cross) -->
    <g id="pixelStar">
      <rect x="2" y="0" width="2" height="6" fill="#fdf2f8" opacity="0.9" />
      <rect x="0" y="2" width="6" height="2" fill="#fdf2f8" opacity="0.9" />
      <rect x="2" y="2" width="2" height="2" fill="#ffffff" />
    </g>
  </defs>

  <style>
    /* Falling Petals Keyframes */
    @keyframes fallSway1 {
      0% {
        transform: translate(0px, -40px) rotate(0deg);
        opacity: 0;
      }
      10% { opacity: 0.95; }
      50% { transform: translate(65px, 160px) rotate(180deg); }
      85% { opacity: 0.9; }
      100% {
        transform: translate(120px, 350px) rotate(360deg);
        opacity: 0;
      }
    }

    @keyframes fallSway2 {
      0% {
        transform: translate(0px, -30px) rotate(0deg);
        opacity: 0;
      }
      15% { opacity: 0.95; }
      50% { transform: translate(-50px, 150px) rotate(-140deg); }
      85% { opacity: 0.9; }
      100% {
        transform: translate(-100px, 350px) rotate(-280deg);
        opacity: 0;
      }
    }

    @keyframes fallSway3 {
      0% {
        transform: translate(0px, -40px) rotate(0deg);
        opacity: 0;
      }
      12% { opacity: 0.9; }
      50% { transform: translate(80px, 170px) rotate(220deg); }
      88% { opacity: 0.85; }
      100% {
        transform: translate(150px, 350px) rotate(420deg);
        opacity: 0;
      }
    }

    .petal-f1 { animation: fallSway1 linear infinite; }
    .petal-f2 { animation: fallSway2 linear infinite; }
    .petal-f3 { animation: fallSway3 linear infinite; }

    /* Pixel Star Twinkle */
    @keyframes starPulse {
      0%, 100% { opacity: 0.25; transform: scale(0.8); }
      50% { opacity: 1; transform: scale(1.2); }
    }
    .pstar {
      transform-box: fill-box;
      transform-origin: center;
      animation: starPulse 2.8s ease-in-out infinite;
    }
    .ps-1 { animation-delay: 0.2s; }
    .ps-2 { animation-delay: 1.1s; animation-duration: 3.4s; }
    .ps-3 { animation-delay: 1.9s; animation-duration: 2.5s; }

    /* Badge Glow Pulse */
    @keyframes badgeGlow {
      0%, 100% { stroke-opacity: 0.5; }
      50% { stroke-opacity: 1; filter: drop-shadow(0 0 8px rgba(255, 117, 151, 0.8)); }
    }
    .sakura-badge {
      animation: badgeGlow 3s ease-in-out infinite;
    }
  </style>

  <!-- Background Sky & Mist -->
  <rect width="1200" height="320" fill="url(#skyGrad)" />
  <rect width="1200" height="320" fill="url(#mist1)" />
  <rect width="1200" height="320" fill="url(#mist2)" />

  <!-- Pixel Stars in Night Sky -->
  <use href="#pixelStar" x="60" y="45" class="pstar ps-1" />
  <use href="#pixelStar" x="140" y="110" class="pstar ps-2" />
  <use href="#pixelStar" x="220" y="35" class="pstar ps-3" />
  <use href="#pixelStar" x="310" y="80" class="pstar ps-1" />
  <use href="#pixelStar" x="410" y="40" class="pstar ps-2" />
  <use href="#pixelStar" x="530" y="65" class="pstar ps-3" />
  <use href="#pixelStar" x="670" y="35" class="pstar ps-1" />
  <use href="#pixelStar" x="780" y="85" class="pstar ps-2" />
  <use href="#pixelStar" x="890" y="45" class="pstar ps-3" />
  <use href="#pixelStar" x="990" y="90" class="pstar ps-1" />
  <use href="#pixelStar" x="1080" y="40" class="pstar ps-2" />
  <use href="#pixelStar" x="1140" y="115" class="pstar ps-3" />

  <use href="#pixelStar" x="95" y="220" class="pstar ps-2" />
  <use href="#pixelStar" x="240" y="260" class="pstar ps-1" />
  <use href="#pixelStar" x="950" y="240" class="pstar ps-3" />
  <use href="#pixelStar" x="1060" y="270" class="pstar ps-1" />

  <!-- Falling Pixel Sakura Petals -->
  <g class="petal-f1" style="animation-duration: 5.5s; animation-delay: 0.1s;">
    <use href="#pixelPetal1" x="80" y="0" />
  </g>
  <g class="petal-f2" style="animation-duration: 6.8s; animation-delay: 1.4s;">
    <use href="#pixelPetal2" x="180" y="0" />
  </g>
  <g class="petal-f3" style="animation-duration: 7.2s; animation-delay: 3.1s;">
    <use href="#pixelBlossom" x="270" y="0" />
  </g>
  <g class="petal-f1" style="animation-duration: 6.0s; animation-delay: 0.8s;">
    <use href="#pixelPetal1" x="390" y="0" />
  </g>
  <g class="petal-f2" style="animation-duration: 5.8s; animation-delay: 2.2s;">
    <use href="#pixelPetal2" x="490" y="0" />
  </g>
  <g class="petal-f3" style="animation-duration: 7.5s; animation-delay: 4.0s;">
    <use href="#pixelPetal1" x="600" y="0" />
  </g>
  <g class="petal-f1" style="animation-duration: 6.4s; animation-delay: 1.8s;">
    <use href="#pixelBlossom" x="710" y="0" />
  </g>
  <g class="petal-f2" style="animation-duration: 5.9s; animation-delay: 0.5s;">
    <use href="#pixelPetal2" x="820" y="0" />
  </g>
  <g class="petal-f3" style="animation-duration: 6.7s; animation-delay: 2.9s;">
    <use href="#pixelPetal1" x="920" y="0" />
  </g>
  <g class="petal-f1" style="animation-duration: 7.0s; animation-delay: 1.1s;">
    <use href="#pixelPetal2" x="1030" y="0" />
  </g>
  <g class="petal-f2" style="animation-duration: 6.2s; animation-delay: 3.6s;">
    <use href="#pixelBlossom" x="1110" y="0" />
  </g>
  <g class="petal-f3" style="animation-duration: 6.5s; animation-delay: 4.8s;">
    <use href="#pixelPetal1" x="150" y="0" />
  </g>
  <g class="petal-f1" style="animation-duration: 5.7s; animation-delay: 2.7s;">
    <use href="#pixelPetal2" x="760" y="0" />
  </g>
  <g class="petal-f2" style="animation-duration: 7.1s; animation-delay: 5.2s;">
    <use href="#pixelPetal1" x="440" y="0" />
  </g>

  <!-- Central Visual Branding / Title -->
  <g text-anchor="middle">
    <!-- Tag Badge: BACKEND ENGINEER -->
    <g transform="translate(600, 68)">
      <rect x="-120" y="-16" width="240" height="32" rx="16" fill="#1c102a" fill-opacity="0.85" stroke="#ff7597" stroke-width="1.5" class="sakura-badge" />
      <circle cx="-90" cy="0" r="4" fill="#ff7597" />
      <text x="8" y="5" fill="#ff7597" font-family="'Courier New', Courier, monospace, sans-serif" font-size="12.5" font-weight="700" letter-spacing="3">🌸 BACKEND ENGINEER</text>
    </g>

    <!-- Main Name: PHI CONG THANH -->
    <text x="600" y="146" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif" font-size="46" font-weight="900" letter-spacing="4" filter="url(#sakuraGlow)">
      PHI CONG THANH
    </text>

    <!-- Secondary Line -->
    <text x="600" y="190" fill="#fda4af" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif" font-size="16" font-weight="500" letter-spacing="2">
      Scalable Architecture • High-Performance Systems • Database Engineering
    </text>

    <!-- Academic Tag: Ho Chi Minh City Open University -->
    <g transform="translate(600, 238)">
      <rect x="-200" y="-15" width="400" height="30" rx="8" fill="#261338" fill-opacity="0.75" stroke="#ff7597" stroke-width="1" />
      <text x="0" y="5" fill="#ffb7c5" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" letter-spacing="0.5">
        🏛️ Ho Chi Minh City Open University (HCMCOU)
      </text>
    </g>
  </g>

  <!-- Bottom Accent Border with Pixel Sakura Tone -->
  <line x1="0" y1="318" x2="1200" y2="318" stroke="#ff7597" stroke-width="2" opacity="0.7" />
</svg>"""

with open('assets/sakura_banner.svg', 'w', encoding='utf-8') as f:
    f.write(banner_svg)

print("assets/sakura_banner.svg written successfully!")

# 2. Generate assets/sakura_footer.svg
footer_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" width="100%" height="100%" preserveAspectRatio="xMidYMid slice">
  <defs>
    <linearGradient id="footerBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b0616" />
      <stop offset="50%" stop-color="#190e2b" />
      <stop offset="100%" stop-color="#0a0514" />
    </linearGradient>

    <!-- Pixel Petal -->
    <g id="fPixelPetal">
      <rect x="2" y="0" width="2" height="2" fill="#ffd1dc" />
      <rect x="4" y="0" width="2" height="2" fill="#ff9ebb" />
      <rect x="0" y="2" width="2" height="2" fill="#ffb7c5" />
      <rect x="2" y="2" width="4" height="4" fill="#ff7597" />
      <rect x="6" y="2" width="2" height="2" fill="#f43f5e" />
      <rect x="2" y="6" width="2" height="2" fill="#ff7597" />
    </g>

    <g id="fPixelStar">
      <rect x="1" y="0" width="1" height="3" fill="#fdf2f8" opacity="0.8" />
      <rect x="0" y="1" width="3" height="1" fill="#fdf2f8" opacity="0.8" />
      <rect x="1" y="1" width="1" height="1" fill="#ffffff" />
    </g>
  </defs>

  <style>
    @keyframes fFall1 {
      0% { transform: translate(0px, -20px) rotate(0deg); opacity: 0; }
      15% { opacity: 0.9; }
      85% { opacity: 0.9; }
      100% { transform: translate(60px, 140px) rotate(240deg); opacity: 0; }
    }
    @keyframes fFall2 {
      0% { transform: translate(0px, -20px) rotate(0deg); opacity: 0; }
      15% { opacity: 0.9; }
      85% { opacity: 0.9; }
      100% { transform: translate(-50px, 140px) rotate(-180deg); opacity: 0; }
    }

    .ff1 { animation: fFall1 4.5s linear infinite; }
    .ff2 { animation: fFall2 5.2s linear infinite; }

    @keyframes fTwinkle {
      0%, 100% { opacity: 0.3; }
      50% { opacity: 1; }
    }
    .fstar { animation: fTwinkle 2.5s ease-in-out infinite; }
  </style>

  <rect width="1200" height="120" fill="url(#footerBg)" />
  <line x1="0" y1="1" x2="1200" y2="1" stroke="#ff7597" stroke-width="1.5" opacity="0.5" />

  <!-- Stars -->
  <use href="#fPixelStar" x="120" y="40" class="fstar" style="animation-delay: 0.3s;" />
  <use href="#fPixelStar" x="350" y="70" class="fstar" style="animation-delay: 1.2s;" />
  <use href="#fPixelStar" x="620" y="30" class="fstar" style="animation-delay: 0.7s;" />
  <use href="#fPixelStar" x="890" y="65" class="fstar" style="animation-delay: 1.8s;" />
  <use href="#fPixelStar" x="1080" y="35" class="fstar" style="animation-delay: 0.5s;" />

  <!-- Drifting Petals -->
  <g class="ff1" style="animation-delay: 0.2s;"><use href="#fPixelPetal" x="180" y="0" /></g>
  <g class="ff2" style="animation-delay: 1.5s;"><use href="#fPixelPetal" x="420" y="0" /></g>
  <g class="ff1" style="animation-delay: 2.8s;"><use href="#fPixelPetal" x="680" y="0" /></g>
  <g class="ff2" style="animation-delay: 0.8s;"><use href="#fPixelPetal" x="930" y="0" /></g>
  <g class="ff1" style="animation-delay: 3.5s;"><use href="#fPixelPetal" x="1100" y="0" /></g>
</svg>"""

with open('assets/sakura_footer.svg', 'w', encoding='utf-8') as f:
    f.write(footer_svg)
print("assets/sakura_footer.svg written successfully!")

# 3. Generate assets/tech_stack.svg (Animated Tech Stack Showcase)
tech_stack_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 220" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <defs>
    <!-- Background Card Gradient -->
    <linearGradient id="cardBgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#120921" />
      <stop offset="50%" stop-color="#1c0f33" />
      <stop offset="100%" stop-color="#10071d" />
    </linearGradient>

    <!-- Glowing Border Gradient -->
    <linearGradient id="sakuraBorder" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff7597" />
      <stop offset="50%" stop-color="#c084fc" />
      <stop offset="100%" stop-color="#ff7597" />
    </linearGradient>

    <!-- Pixel Petal -->
    <g id="tPixelPetal">
      <rect x="2" y="0" width="2" height="2" fill="#ffd1dc" />
      <rect x="4" y="0" width="2" height="2" fill="#ff9ebb" />
      <rect x="0" y="2" width="2" height="2" fill="#ffb7c5" />
      <rect x="2" y="2" width="4" height="4" fill="#ff7597" />
      <rect x="6" y="2" width="2" height="2" fill="#f43f5e" />
      <rect x="2" y="6" width="2" height="2" fill="#ff7597" />
    </g>
  </defs>

  <style>
    /* Floating Card Animations with Stagger */
    @keyframes floatCard1 {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-7px); }
    }
    @keyframes floatCard2 {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-7px); }
    }
    @keyframes floatCard3 {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-7px); }
    }
    @keyframes floatCard4 {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-7px); }
    }

    .fcard-1 { animation: floatCard1 3.4s ease-in-out infinite; }
    .fcard-2 { animation: floatCard2 3.8s ease-in-out infinite 0.5s; }
    .fcard-3 { animation: floatCard3 3.6s ease-in-out infinite 1.0s; }
    .fcard-4 { animation: floatCard4 4.0s ease-in-out infinite 1.5s; }

    /* Pulsing Glow */
    @keyframes pulseCardBorder {
      0%, 100% { stroke-opacity: 0.4; }
      50% { stroke-opacity: 0.95; filter: drop-shadow(0 0 6px rgba(255, 117, 151, 0.6)); }
    }
    .p-border { animation: pulseCardBorder 3s ease-in-out infinite; }

    /* Drifting Petals */
    @keyframes tPetalFall {
      0% { transform: translate(0, -20px) rotate(0deg); opacity: 0; }
      15% { opacity: 0.85; }
      85% { opacity: 0.85; }
      100% { transform: translate(45px, 240px) rotate(220deg); opacity: 0; }
    }
    .tpetal { animation: tPetalFall 5.5s linear infinite; }
  </style>

  <!-- Container Box -->
  <rect width="920" height="220" rx="16" fill="url(#cardBgGrad)" stroke="#2e1845" stroke-width="1.5" />

  <!-- Floating Sakura Petals across Tech Stack -->
  <g class="tpetal" style="animation-delay: 0.2s;"><use href="#tPixelPetal" x="70" y="0" /></g>
  <g class="tpetal" style="animation-delay: 1.8s;"><use href="#tPixelPetal" x="290" y="0" /></g>
  <g class="tpetal" style="animation-delay: 3.2s;"><use href="#tPixelPetal" x="510" y="0" /></g>
  <g class="tpetal" style="animation-delay: 0.9s;"><use href="#tPixelPetal" x="730" y="0" /></g>
  <g class="tpetal" style="animation-delay: 2.5s;"><use href="#tPixelPetal" x="840" y="0" /></g>

  <!-- Section Title -->
  <g text-anchor="middle">
    <text x="460" y="32" fill="#ff7597" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="800" letter-spacing="3">
      ⚡ TECH STACK &amp; CAPABILITIES ⚡
    </text>
  </g>

  <!-- 4 Interactive Floating Skill Cards -->
  
  <!-- Card 1: Core & Backend (Java, C++) -->
  <g class="fcard-1" transform="translate(30, 50)">
    <rect width="200" height="145" rx="12" fill="#170d2b" stroke="url(#sakuraBorder)" stroke-width="1.4" class="p-border" />
    <rect width="200" height="32" rx="12" fill="#24143f" />
    <text x="100" y="21" text-anchor="middle" fill="#ffb7c5" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="700">☕ Core &amp; Backend</text>
    
    <!-- Java Badge -->
    <g transform="translate(18, 48)">
      <rect width="164" height="36" rx="8" fill="#0d071a" stroke="#3d2159" stroke-width="1" />
      <circle cx="20" cy="18" r="5" fill="#f89820" />
      <text x="34" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="700">Java</text>
      <text x="148" y="22" fill="#a855f7" font-family="monospace" font-size="10">CORE</text>
    </g>

    <!-- C++ Badge -->
    <g transform="translate(18, 94)">
      <rect width="164" height="36" rx="8" fill="#0d071a" stroke="#3d2159" stroke-width="1" />
      <circle cx="20" cy="18" r="5" fill="#00599c" />
      <text x="34" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="700">C++</text>
      <text x="135" y="22" fill="#38bdf8" font-family="monospace" font-size="10">PERF</text>
    </g>
  </g>

  <!-- Card 2: Databases (PostgreSQL, SQL) -->
  <g class="fcard-2" transform="translate(250, 50)">
    <rect width="200" height="145" rx="12" fill="#170d2b" stroke="url(#sakuraBorder)" stroke-width="1.4" class="p-border" />
    <rect width="200" height="32" rx="12" fill="#24143f" />
    <text x="100" y="21" text-anchor="middle" fill="#ffb7c5" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="700">🗄️ Databases</text>

    <!-- PostgreSQL Badge -->
    <g transform="translate(18, 48)">
      <rect width="164" height="36" rx="8" fill="#0d071a" stroke="#3d2159" stroke-width="1" />
      <circle cx="20" cy="18" r="5" fill="#4169e1" />
      <text x="34" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="700">PostgreSQL</text>
      <text x="145" y="22" fill="#60a5fa" font-family="monospace" font-size="10">RDBMS</text>
    </g>

    <!-- SQL Badge -->
    <g transform="translate(18, 94)">
      <rect width="164" height="36" rx="8" fill="#0d071a" stroke="#3d2159" stroke-width="1" />
      <circle cx="20" cy="18" r="5" fill="#336791" />
      <text x="34" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="700">SQL</text>
      <text x="138" y="22" fill="#93c5fd" font-family="monospace" font-size="10">QUERY</text>
    </g>
  </g>

  <!-- Card 3: Tools & OS (Git, GitHub, Linux, VS Code) -->
  <g class="fcard-3" transform="translate(470, 50)">
    <rect width="200" height="145" rx="12" fill="#170d2b" stroke="url(#sakuraBorder)" stroke-width="1.4" class="p-border" />
    <rect width="200" height="32" rx="12" fill="#24143f" />
    <text x="100" y="21" text-anchor="middle" fill="#ffb7c5" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="700">🛠️ Tools &amp; OS</text>

    <!-- Git & GitHub -->
    <g transform="translate(18, 48)">
      <rect width="164" height="36" rx="8" fill="#0d071a" stroke="#3d2159" stroke-width="1" />
      <circle cx="20" cy="18" r="5" fill="#f05032" />
      <text x="34" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="700">Git / GitHub</text>
      <text x="140" y="22" fill="#f87171" font-family="monospace" font-size="10">VCS</text>
    </g>

    <!-- Linux & VS Code -->
    <g transform="translate(18, 94)">
      <rect width="164" height="36" rx="8" fill="#0d071a" stroke="#3d2159" stroke-width="1" />
      <circle cx="20" cy="18" r="5" fill="#007acc" />
      <text x="34" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="700">Linux / VS Code</text>
      <text x="142" y="22" fill="#38bdf8" font-family="monospace" font-size="10">ENV</text>
    </g>
  </g>

  <!-- Card 4: 3D Graphics (Blender) -->
  <g class="fcard-4" transform="translate(690, 50)">
    <rect width="200" height="145" rx="12" fill="#170d2b" stroke="url(#sakuraBorder)" stroke-width="1.4" class="p-border" />
    <rect width="200" height="32" rx="12" fill="#24143f" />
    <text x="100" y="21" text-anchor="middle" fill="#ffb7c5" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="700">🎨 3D &amp; Creative</text>

    <!-- Blender Badge -->
    <g transform="translate(18, 48)">
      <rect width="164" height="36" rx="8" fill="#0d071a" stroke="#3d2159" stroke-width="1" />
      <circle cx="20" cy="18" r="5" fill="#e87d0d" />
      <text x="34" y="22" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="700">Blender</text>
      <text x="145" y="22" fill="#fb923c" font-family="monospace" font-size="10">3D</text>
    </g>

    <!-- 3D Modeling Tag -->
    <g transform="translate(18, 94)">
      <rect width="164" height="36" rx="8" fill="#0d071a" stroke="#3d2159" stroke-width="1" />
      <circle cx="20" cy="18" r="5" fill="#ec4899" />
      <text x="34" y="22" fill="#e2e8f0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" font-weight="600">3D Modeling</text>
      <text x="140" y="22" fill="#f472b6" font-family="monospace" font-size="10">ART</text>
    </g>
  </g>
</svg>"""

with open('assets/tech_stack.svg', 'w', encoding='utf-8') as f:
    f.write(tech_stack_svg)
print("assets/tech_stack.svg written successfully!")
