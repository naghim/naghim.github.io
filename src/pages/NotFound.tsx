import { useLocation } from "react-router-dom";
import { useEffect } from "react";
import heroImage from "@/assets/floral-hero.jpg";

const NotFound = () => {
  const location = useLocation();

  useEffect(() => {
    console.error("404 Error: User attempted to access non-existent route:", location.pathname);
  }, [location.pathname]);

  return (
    <div className="h-screen relative overflow-hidden bg-soft-white">
      {/* Diagonal Floral Section */}
      <div className="absolute inset-0 w-full h-full">
        {/* Main floral background with diagonal cut */}
        <div className="absolute left-0 top-0 h-full w-[100%] md:w-[45%] md:clip-diagonal clip-none">
          <img
            src={heroImage}
            alt="Background decoration"
            className="w-full h-full object-cover object-right scale-110"
          />
          <div className="absolute inset-0 bg-gradient-to-br from-transparent via-transparent to-soft-white/30" />
        </div>
      </div>

      {/* Content Section */}
      <div className="relative z-10 h-screen flex items-center justify-center md:justify-end gap-x-6 p-2 lg:pr-24">
        <div
          style={{ backgroundColor: "hsla(0, 0%, 98%, 0.80)" }}
          className="backdrop-blur-sm w-full md:w-[55%] lg:w-[50%] p-6 md:p-10 lg:p-[3rem] animate-fade-in-right max-w-2xl rounded-xl "
        >
          <p className="leading-tight font-sans text-4xl font-serif text-muted-foreground leading-relaxed">
            <span className="text-5xl italic">Whoopsie!</span> <br /> Page not found.
          </p>
        </div>
      </div>
    </div>
  );
};

export default NotFound;
