import { Mail } from "lucide-react";

const ContactInfoSection = () => (
  <div className="mb-5 flex flex-wrap gap-x-6 gap-y-2 text-sm">
    <a
      href="mailto:mirtill@naghi.me"
      className="flex items-center gap-2 text-foreground hover:text-sage transition-colors group"
    >
      <Mail className="w-4 h-4 text-burgundy" />
      <span className="font-sans group-hover:underline">mirtill@naghi.me</span>
    </a>
    <a
      href="https://naghi.me"
      target="_blank"
      rel="noopener noreferrer"
      className="text-burgundy hover:text-sage transition-colors hover:underline"
    >
      naghi.me
    </a>
  </div>
);

export default ContactInfoSection;
