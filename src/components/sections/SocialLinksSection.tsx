import { Button } from "@/components/ui/button";
import { Github } from "lucide-react";

const SocialLinksSection = () => (
  <div className="flex items-center justify-center gap-2">
    <Button
      variant="outline"
      size="icon"
      className="rounded-full border-sage hover:bg-sage hover:text-white transition-all h-9 w-9"
      asChild
    >
      <a
        href="https://scholar.google.com/citations?user=hHjKdUkAAAAJ"
        target="_blank"
        rel="noopener noreferrer"
        title="Google Scholar"
      >
        <svg className="w-4 h-4" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 24a7 7 0 1 1 0-14 7 7 0 0 1 0 14zm0-24L0 9.5l4.838 3.94A8 8 0 0 1 12 9a8 8 0 0 1 7.162 4.44L24 9.5z" />
        </svg>
      </a>
    </Button>
    <Button
      variant="outline"
      size="icon"
      className="rounded-full border-sage hover:bg-sage hover:text-white transition-all h-9 w-9"
      asChild
    >
      <a
        href="https://github.com/naghim"
        target="_blank"
        rel="noopener noreferrer"
        title="GitHub"
      >
        <Github className="w-4 h-4" />
      </a>
    </Button>
    <Button
      variant="outline"
      size="icon"
      className="rounded-full border-sage hover:bg-sage hover:text-white transition-all h-9 w-9"
      asChild
    >
      <a
        href="https://ieeexplore.ieee.org/author/37089731404"
        target="_blank"
        rel="noopener noreferrer"
        title="IEEE Xplore"
      >
        <svg
          version="1.0"
          xmlns="http://www.w3.org/2000/svg"
          width="300.000000pt"
          height="300.000000pt"
          viewBox="0 0 300.000000 300.000000"
          preserveAspectRatio="xMidYMid meet"
        >
          <g
            transform="translate(0.000000,293.000000) scale(0.100000,-0.100000)"
            fill="currentColor"
          >
            <path
              d="M1437 2911 c-16 -10 -52 -54 -82 -97 -85 -127 -338 -408 -630 -700
-281 -281 -412 -395 -556 -482 -118 -71 -139 -94 -139 -150 0 -40 5 -49 43
-86 24 -22 86 -68 138 -101 319 -202 767 -652 1112 -1117 97 -131 117 -148
166 -148 41 0 60 19 190 195 287 387 814 894 1197 1153 100 67 110 131 28 180
-201 121 -353 242 -578 462 -262 257 -501 525 -680 763 -110 146 -147 169
-209 128z m113 -374 c76 -31 154 -85 290 -198 302 -251 595 -574 693 -764 58
-114 37 -185 -112 -374 -169 -213 -611 -631 -801 -757 -88 -59 -130 -65 -200
-30 -245 123 -866 721 -995 958 -52 95 -34 157 94 328 157 209 572 617 776
762 73 53 159 98 185 98 8 0 40 -11 70 -23z"
            />
            <path
              d="M1402 2453 c-201 -122 -692 -600 -858 -835 -73 -103 -88 -141 -74
-182 47 -135 468 -579 780 -823 108 -84 221 -153 250 -153 99 0 715 570 923
855 16 22 40 62 54 90 24 46 25 54 14 94 -42 159 -463 616 -806 877 -85 65
-172 114 -203 114 -10 0 -46 -17 -80 -37z m177 -432 c50 -118 91 -218 91 -223
0 -4 -30 -8 -66 -8 l-66 0 6 -52 c3 -29 7 -129 8 -223 l2 -170 -73 -3 -74 -3
4 223 4 223 -47 3 c-27 2 -48 6 -48 9 0 8 124 386 140 427 6 17 14 25 19 20 5
-5 50 -105 100 -223z m-367 -357 c43 -25 78 -47 78 -49 0 -1 -26 -13 -57 -26
-212 -84 -201 -179 27 -250 66 -21 95 -23 230 -23 135 1 168 4 258 28 139 36
202 77 202 132 0 10 -20 37 -45 60 -41 40 -49 43 -107 46 l-62 3 -17 50 c-14
41 -15 51 -4 53 13 3 264 -63 272 -72 3 -2 -5 -7 -17 -11 -19 -6 -18 -9 19
-35 82 -60 92 -107 35 -170 -46 -50 -173 -114 -274 -137 -55 -12 -120 -17
-240 -17 -198 0 -355 26 -477 77 -227 96 -262 191 -108 297 40 27 177 89 199
90 5 0 45 -21 88 -46z m358 -541 c0 -49 3 -152 7 -230 l6 -143 -101 0 c-55 0
-103 4 -106 9 -6 9 22 414 29 439 3 8 29 12 85 12 l80 0 0 -87z"
            />
          </g>
        </svg>
      </a>
    </Button>
  </div>
);

export default SocialLinksSection;
