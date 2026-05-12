





import java.util.List;
import java.util.ArrayList;

public class Reqtify_Section extends TextElement {






    private Document document;




    private List<Section> sections;




    private Section section;


    public Reqtify_Section(
    ) {
        super(
        );
        this.sections = new ArrayList<>();
    }

    public Reqtify_Section(
        ArrayList<Section> sections    ) {
        this.sections = sections;
    }


    public Document getDocument() {
        return document;
    }

    public void setDocument(Document document) {
        this.document = document;
    }
    public List<Section> getSections() {
        return sections;
    }

    public void addSection(Section section) {
        this.sections.add(section);
    }
    public Section getSection() {
        return section;
    }

    public void setSection(Section section) {
        this.section = section;
    }

}