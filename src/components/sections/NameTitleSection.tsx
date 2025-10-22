import { Sparkles } from "lucide-react";

const NameTitleSection = () => (
  <div className="mb-6">
    <div className="flex items-center gap-2 mb-3">
      <Sparkles className="w-5 h-5 text-burgundy animate-pulse" />
      <span className="text-xs font-semibold text-burgundy uppercase tracking-widest">
        Researcher • Educator • Developer
      </span>
    </div>
    <h1 className="font-serif text-4xl md:text-5xl lg:text-6xl font-bold text-foreground mb-3 leading-tight">
      Mirtill - Boglárka <span className="">Naghi</span>
    </h1>
    <p className="font-serif text-lg md:text-2xl text-muted-foreground font-light italic tracking-wide">
      Turning complex algorithms into practical tools.
    </p>
  </div>
);

export default NameTitleSection;
