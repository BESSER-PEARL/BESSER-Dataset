





import java.util.List;
import java.util.ArrayList;

public class uma_Section extends VariabilityElement {

    private String sectionName;
    private String sectionDescription;





    private uma_Section uma_section;




    private List<uma_Section> uma_sections;


    public uma_Section(
        String sectionName,        String sectionDescription    ) {
        super(
        );
        this.sectionName = sectionName;
        this.sectionDescription = sectionDescription;
        this.uma_sections = new ArrayList<>();
    }

    public uma_Section(
        String sectionName,        String sectionDescription        ArrayList<uma_Section> uma_sections    ) {
        this.sectionName = sectionName;
        this.sectionDescription = sectionDescription;
        this.uma_sections = uma_sections;
    }

    public String getSectionname() {
        return sectionName;
    }

    public void setSectionname(String sectionName) {
        this.sectionName = sectionName;
    }
    public String getSectiondescription() {
        return sectionDescription;
    }

    public void setSectiondescription(String sectionDescription) {
        this.sectionDescription = sectionDescription;
    }

    public uma_Section getUma_section() {
        return uma_section;
    }

    public void setUma_section(uma_Section uma_section) {
        this.uma_section = uma_section;
    }
    public List<uma_Section> getUma_sections() {
        return uma_sections;
    }

    public void addUma_section(Uma_section uma_section) {
        this.uma_sections.add(uma_section);
    }

}