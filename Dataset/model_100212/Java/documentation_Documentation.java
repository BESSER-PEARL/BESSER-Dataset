





import java.util.List;
import java.util.ArrayList;

public class documentation_Documentation  {

    private String title;





    private List<documentation_Section> documentation_sections;




    private List<documentation_TermEntry> documentation_termentrys;


    public documentation_Documentation(
        String title    ) {
        this.title = title;
        this.documentation_sections = new ArrayList<>();
        this.documentation_termentrys = new ArrayList<>();
    }

    public documentation_Documentation(
        String title        ArrayList<documentation_Section> documentation_sections,        ArrayList<documentation_TermEntry> documentation_termentrys    ) {
        this.title = title;
        this.documentation_sections = documentation_sections;
        this.documentation_termentrys = documentation_termentrys;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<documentation_Section> getDocumentation_sections() {
        return documentation_sections;
    }

    public void addDocumentation_section(Documentation_section documentation_section) {
        this.documentation_sections.add(documentation_section);
    }
    public List<documentation_TermEntry> getDocumentation_termentrys() {
        return documentation_termentrys;
    }

    public void addDocumentation_termentry(Documentation_termentry documentation_termentry) {
        this.documentation_termentrys.add(documentation_termentry);
    }

}