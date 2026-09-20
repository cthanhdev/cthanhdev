import os

os.makedirs('assets', exist_ok=True)

# Common SVG Defs for watercolor sakura petals and blossoms
SAKURA_DEFS = """
    <!-- Gradients for Sakura Petals -->
    <linearGradient id="petalGrad" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#ff7597" />
      <stop offset="45%" stop-color="#ffb7c5" />
      <stop offset="90%" stop-color="#fff0f5" />
      <stop offset="100%" stop-color="#ffffff" />
    </linearGradient>

    <radialGradient id="blossomCenter" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="35%" stop-color="#f43f5e" />
      <stop offset="70%" stop-color="#ff7597" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#ffb7c5" stop-opacity="0" />
    </radialGradient>

    <linearGradient id="branchGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#422518" />
      <stop offset="50%" stop-color="#5c382b" />
      <stop offset="100%" stop-color="#3d2116" />
    </linearGradient>

    <linearGradient id="ribbonGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fb7185" />
      <stop offset="50%" stop-color="#f472b6" />
      <stop offset="100%" stop-color="#c084fc" />
    </linearGradient>

    <!-- Glow & Soft Filters -->
    <filter id="sakuraGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="5" result="blur" />
      <feFlood flood-color="#ff7597" flood-opacity="0.65" result="flood" />
      <feComposite in="flood" in2="blur" operator="in" result="glow" />
      <feMerge>
        <feMergeNode in="glow" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="bokehBlur" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3.5" />
    </filter>

    <!-- Single Realistic Notched Sakura Petal (Like reference images 1, 2, 3) -->
    <g id="sakuraPetal">
      <path d="M 0,0 C -7,-10 -13,-22 -5,-28 C -2,-26 0,-24 0,-24 C 0,-24 2,-26 5,-28 C 13,-22 7,-10 0,0 Z" fill="url(#petalGrad)" />
      <!-- Soft center vein -->
      <line x1="0" y1="-2" x2="0" y2="-18" stroke="#f43f5e" stroke-width="0.8" opacity="0.4" />
    </g>

    <!-- Full 5-Petal Blooming Cherry Blossom (Like reference images 1 & 4) -->
    <g id="cherryBlossom">
      <!-- 5 Petals rotated at 72 deg increments -->
      <g transform="rotate(0)"><use href="#sakuraPetal" /></g>
      <g transform="rotate(72)"><use href="#sakuraPetal" /></g>
      <g transform="rotate(144)"><use href="#sakuraPetal" /></g>
      <g transform="rotate(216)"><use href="#sakuraPetal" /></g>
      <g transform="rotate(288)"><use href="#sakuraPetal" /></g>
      <!-- Blossom Center with Pistils & Stamens -->
      <circle cx="0" cy="0" r="5" fill="url(#blossomCenter)" />
      <!-- Tiny pistil rays -->
      <circle cx="0" cy="0" r="2.2" fill="#fbbf24" />
      <circle cx="-3" cy="-3" r="0.9" fill="#f59e0b" />
      <circle cx="3" cy="-3" r="0.9" fill="#f59e0b" />
      <circle cx="-4" cy="2" r="0.9" fill="#f59e0b" />
      <circle cx="4" cy="2" r="0.9" fill="#f59e0b" />
      <circle cx="0" cy="4" r="0.9" fill="#f59e0b" />
    </g>

    <!-- Small Flower Bud -->
    <g id="sakuraBud">
      <path d="M 0,0 C -3,-5 -3,-10 0,-13 C 3,-10 3,-5 0,0 Z" fill="#ff7597" />
      <path d="M -2,0 C -2,-3 0,-5 0,-5 C 0,-5 2,-3 2,0 Z" fill="#65a30d" opacity="0.8" />
    </g>
"""

print("Defs created successfully.")
