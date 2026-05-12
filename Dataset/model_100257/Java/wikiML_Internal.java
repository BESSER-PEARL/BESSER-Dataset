





import java.util.List;
import java.util.ArrayList;

public class wikiML_Internal extends HyperLink {






    private wikiML_Text wikiml_text;




    private wikiML_WikiPage wikiml_wikipage;


    public wikiML_Internal(
    ) {
        super(
        );
    }



    public wikiML_Text getWikiml_text() {
        return wikiml_text;
    }

    public void setWikiml_text(wikiML_Text wikiml_text) {
        this.wikiml_text = wikiml_text;
    }
    public wikiML_WikiPage getWikiml_wikipage() {
        return wikiml_wikipage;
    }

    public void setWikiml_wikipage(wikiML_WikiPage wikiml_wikipage) {
        this.wikiml_wikipage = wikiml_wikipage;
    }

}