





import java.util.List;
import java.util.ArrayList;

public class wikiML_Paragraph extends ParagraphTypes {

    private String paragraph;





    private wikiML_UnorderedList wikiml_unorderedlist;




    private wikiML_OrderedList wikiml_orderedlist;


    public wikiML_Paragraph(
        String paragraph    ) {
        super(
        );
        this.paragraph = paragraph;
    }


    public String getParagraph() {
        return paragraph;
    }

    public void setParagraph(String paragraph) {
        this.paragraph = paragraph;
    }

    public wikiML_UnorderedList getWikiml_unorderedlist() {
        return wikiml_unorderedlist;
    }

    public void setWikiml_unorderedlist(wikiML_UnorderedList wikiml_unorderedlist) {
        this.wikiml_unorderedlist = wikiml_unorderedlist;
    }
    public wikiML_OrderedList getWikiml_orderedlist() {
        return wikiml_orderedlist;
    }

    public void setWikiml_orderedlist(wikiML_OrderedList wikiml_orderedlist) {
        this.wikiml_orderedlist = wikiml_orderedlist;
    }

}