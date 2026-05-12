





import java.util.List;
import java.util.ArrayList;

public class wikiML_MainTemplate extends Template {






    private List<wikiML_AnyTextSequence> wikiml_anytextsequences;


    public wikiML_MainTemplate(
    ) {
        super(
        );
        this.wikiml_anytextsequences = new ArrayList<>();
    }

    public wikiML_MainTemplate(
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