





import java.util.List;
import java.util.ArrayList;

public class Documentation_Book  {

    private String title;





    private List<Documentation_Section> documentation_sections;


    public Documentation_Book(
        String title    ) {
        this.title = title;
        this.documentation_sections = new ArrayList<>();
    }

    public Documentation_Book(
        String title        ArrayList<Documentation_Section> documentation_sections    ) {
        this.title = title;
        this.documentation_sections = documentation_sections;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<Documentation_Section> getDocumentation_sections() {
        return documentation_sections;
    }

    public void addDocumentation_section(Documentation_section documentation_section) {
        this.documentation_sections.add(documentation_section);
    }

}