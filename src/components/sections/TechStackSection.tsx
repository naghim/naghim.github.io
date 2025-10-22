import { Badge } from "@/components/ui/badge";

export type TechStackSectionProps = {
  expertise: string[];
};

const TechStackSection = ({ expertise }: TechStackSectionProps) => (
  <div className="mb-6">
    <h3 className="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-2">
      Tech Stack
    </h3>
    <div className="flex flex-wrap gap-2">
      {expertise.map((tech) => (
        <Badge
          key={tech}
          className="bg-burgundy/10 text-burgundy border-burgundy/20 hover:bg-burgundy hover:text-white transition-all cursor-default"
        >
          {tech}
        </Badge>
      ))}
    </div>
  </div>
);

export default TechStackSection;
