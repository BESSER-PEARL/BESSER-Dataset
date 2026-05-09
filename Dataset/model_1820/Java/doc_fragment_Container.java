





import java.util.List;
import java.util.ArrayList;

public class doc_fragment_Container  {

    private String content;





    private List<Content> contents;




    private List<Section> sections;


    public doc_fragment_Container(
        String content    ) {
        this.content = content;
        this.contents = new ArrayList<>();
        this.sections = new ArrayList<>();
    }

    public doc_fragment_Container(
        String content        ArrayList<Content> contents,        ArrayList<Section> sections    ) {
        this.content = content;
        this.contents = contents;
        this.sections = sections;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public List<Content> getContents() {
        return contents;
    }

    public void addContent(Content content) {
        this.contents.add(content);
    }
    public List<Section> getSections() {
        return sections;
    }

    public void addSection(Section section) {
        this.sections.add(section);
    }

}