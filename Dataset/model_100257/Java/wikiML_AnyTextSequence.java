





import java.util.List;
import java.util.ArrayList;

public class wikiML_AnyTextSequence  {






    private wikiML_BlockQuote wikiml_blockquote;




    private wikiML_Image wikiml_image;




    private List<wikiML_AnyText> wikiml_anytexts;


    public wikiML_AnyTextSequence(
    ) {
        this.wikiml_anytexts = new ArrayList<>();
    }

    public wikiML_AnyTextSequence(
        ArrayList<wikiML_AnyText> wikiml_anytexts    ) {
        this.wikiml_anytexts = wikiml_anytexts;
    }


    public wikiML_BlockQuote getWikiml_blockquote() {
        return wikiml_blockquote;
    }

    public void setWikiml_blockquote(wikiML_BlockQuote wikiml_blockquote) {
        this.wikiml_blockquote = wikiml_blockquote;
    }
    public wikiML_Image getWikiml_image() {
        return wikiml_image;
    }

    public void setWikiml_image(wikiML_Image wikiml_image) {
        this.wikiml_image = wikiml_image;
    }
    public List<wikiML_AnyText> getWikiml_anytexts() {
        return wikiml_anytexts;
    }

    public void addWikiml_anytext(Wikiml_anytext wikiml_anytext) {
        this.wikiml_anytexts.add(wikiml_anytext);
    }

}