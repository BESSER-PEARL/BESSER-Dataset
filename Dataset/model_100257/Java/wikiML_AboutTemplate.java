





import java.util.List;
import java.util.ArrayList;

public class wikiML_AboutTemplate extends Template {






    private List<wikiML_AnyTextSequence> wikiml_anytextsequences;


    public wikiML_AboutTemplate(
    ) {
        super(
        );
        this.wikiml_anytextsequences = new ArrayList<>();
    }

    public wikiML_AboutTemplate(
        ArrayList<wikiML_AnyTextSequence> wikiml_anytextsequences    ) {
        this.wikiml_anytextsequences = wikiml_anytextsequences;
    }


    public List<wikiML_AnyTextSequence> getWikiml_anytextsequences() {
        return wikiml_anytextsequences;
    }

    public void addWikiml_anytextsequence(Wikiml_anytextsequence wikiml_anytextsequence) {
        this.wikiml_anytextsequences.add(wikiml_anytextsequence);
    }

}