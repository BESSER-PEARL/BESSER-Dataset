





import java.util.List;
import java.util.ArrayList;

public class uma_Section extends VariabilityElement {

    private String sectionDescription;
    private String sectionName;





    private uma_Section uma_section;




    private uma_ContentDescription uma_contentdescription;




    private List<uma_Section> uma_sections;


    public uma_Section(
        String sectionDescription,        String sectionName    ) {
        super(
        );
        this.sectionDescription = sectionDescription;
        this.sectionName = sectionName;
        this.uma_sections = new ArrayList<>();
    }

    public uma_Section(
        String sectionDescription,        String sectionName        ArrayList<uma_Section> uma_sections    ) {
        this.sectionDescription = sectionDescription;
        this.sectionName = sectionName;
        this.uma_sections = uma_sections;
    }

    public String getSectiondescription() {
        return sectionDescription;
    }

    public void setSectiondescription(String sectionDescription) {
        this.sectionDescription = sectionDescription;
    }
    public String getSectionname() {
        return sectionName;
    }

    public void setSectionname(String sectionName) {
        this.sectionName = sectionName;
    }

    public uma_Section getUma_section() {
        return uma_section;
    }

    public void setUma_section(uma_Section uma_section) {
        this.uma_section = uma_section;
    }
    public uma_ContentDescription getUma_contentdescription() {
        return uma_contentdescription;
    }

    public void setUma_contentdescription(uma_ContentDescription uma_contentdescription) {
        this.uma_contentdescription = uma_contentdescription;
    }
    public List<uma_Section> getUma_sections() {
        return uma_sections;
    }

    public void addUma_section(Uma_section uma_section) {
        this.uma_sections.add(uma_section);
    }

}