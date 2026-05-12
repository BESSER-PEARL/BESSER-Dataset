





import java.util.List;
import java.util.ArrayList;

public class wikiML_UnorderListItem  {

    private String level;





    private wikiML_AnyTextSequence wikiml_anytextsequence;




    private wikiML_UnorderedList wikiml_unorderedlist;


    public wikiML_UnorderListItem(
        String level    ) {
        this.level = level;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }

    public wikiML_AnyTextSequence getWikiml_anytextsequence() {
        return wikiml_anytextsequence;
    }

    public void setWikiml_anytextsequence(wikiML_AnyTextSequence wikiml_anytextsequence) {
        this.wikiml_anytextsequence = wikiml_anytextsequence;
    }
    public wikiML_UnorderedList getWikiml_unorderedlist() {
        return wikiml_unorderedlist;
    }

    public void setWikiml_unorderedlist(wikiML_UnorderedList wikiml_unorderedlist) {
        this.wikiml_unorderedlist = wikiml_unorderedlist;
    }

}