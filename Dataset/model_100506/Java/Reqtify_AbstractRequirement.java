





import java.util.List;
import java.util.ArrayList;

public class Reqtify_AbstractRequirement extends TextElement {






    private List<Attribute> attributes;




    private List<CoverLink> coverlinks;




    private MacroRequirement macrorequirement;




    private Section section;


    public Reqtify_AbstractRequirement(
    ) {
        super(
        );
        this.attributes = new ArrayList<>();
        this.coverlinks = new ArrayList<>();
    }

    public Reqtify_AbstractRequirement(
        ArrayList<Attribute> attributes,        ArrayList<CoverLink> coverlinks    ) {
        this.attributes = attributes;
        this.coverlinks = coverlinks;
    }


    public List<Attribute> getAttributes() {
        return attributes;
    }

    public void addAttribute(Attribute attribute) {
        this.attributes.add(attribute);
    }
    public List<CoverLink> getCoverlinks() {
        return coverlinks;
    }

    public void addCoverlink(Coverlink coverlink) {
        this.coverlinks.add(coverlink);
    }
    public MacroRequirement getMacrorequirement() {
        return macrorequirement;
    }

    public void setMacrorequirement(MacroRequirement macrorequirement) {
        this.macrorequirement = macrorequirement;
    }
    public Section getSection() {
        return section;
    }

    public void setSection(Section section) {
        this.section = section;
    }

}