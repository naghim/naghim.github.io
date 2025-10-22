import { Mail, Github } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import heroImage from "@/assets/floral-hero.jpg";

import AboutSection from "./sections/AboutSection";
import NameTitleSection from "./sections/NameTitleSection";
import InterestsSection from "./sections/InterestsSection";
import TechStackSection from "./sections/TechStackSection";
import ContactInfoSection from "./sections/ContactInfoSection";
import SocialLinksSection from "./sections/SocialLinksSection";

const Main = () => {
  const interests = [
    "Fuzzy Clustering",
    "Machine Learning",
    "Web Development",
    "UI/UX Design",
  ];
  const expertise = ["C++", "Python", "React"];

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
          {/* Name & Title */}
          <NameTitleSection />
          {/* Divider */}
          <div className="w-20 h-px bg-sage mb-5" />
          {/* About */}
          <AboutSection />
          {/* Interests Tags */}
          <InterestsSection interests={interests} />
          {/* Expertise Tags */}
          <TechStackSection expertise={expertise} />
          {/* Contact Info - Compact */}
          <ContactInfoSection />
          {/* Social Links */}
          <SocialLinksSection />
        </div>
      </div>
    </div>
  );
};

export default Main;
