import { Badge } from "@/components/ui/badge";

export type InterestsSectionProps = {
  interests: string[];
};

const InterestsSection = ({ interests }: InterestsSectionProps) => (
  <div className="mb-5">
    <h3 className="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-2">
      Research / Interests
    </h3>
    <div className="flex flex-wrap gap-2">
      {interests.map((interest) => (
        <Badge
          key={interest}
          variant="outline"
          className="border-sage/40 text-sage hover:bg-sage hover:text-white transition-all cursor-default"
        >
          {interest}
        </Badge>
      ))}
    </div>
  </div>
);

export default InterestsSection;
