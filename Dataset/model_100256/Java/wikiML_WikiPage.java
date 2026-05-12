





import java.util.List;
import java.util.ArrayList;

public class wikiML_WikiPage  {

    private String name;





    private List<wikiML_ParagraphTypes> wikiml_paragraphtypess;


    public wikiML_WikiPage(
        String name    ) {
        this.name = name;
        this.wikiml_paragraphtypess = new ArrayList<>();
    }

    public wikiML_WikiPage(
        String name        ArrayList<wikiML_ParagraphTypes> wikiml_paragraphtypess    ) {
        this.name = name;
        this.wikiml_paragraphtypess = wikiml_paragraphtypess;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<wikiML_ParagraphTypes> getWikiml_paragraphtypess() {
        return wikiml_paragraphtypess;
    }

    public void addWikiml_paragraphtypes(Wikiml_paragraphtypes wikiml_paragraphtypes) {
        this.wikiml_paragraphtypess.add(wikiml_paragraphtypes);
    }

}