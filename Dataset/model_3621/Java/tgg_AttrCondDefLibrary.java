





import java.util.List;
import java.util.ArrayList;

public class tgg_AttrCondDefLibrary extends NamedElements {






    private List<tgg_AttrCondDef> tgg_attrconddefs;




    private tgg_TripleGraphGrammarFile tgg_triplegraphgrammarfile;


    public tgg_AttrCondDefLibrary(
    ) {
        super(
        );
        this.tgg_attrconddefs = new ArrayList<>();
    }

    public tgg_AttrCondDefLibrary(
        ArrayList<tgg_AttrCondDef> tgg_attrconddefs    ) {
        this.tgg_attrconddefs = tgg_attrconddefs;
    }


    public List<tgg_AttrCondDef> getTgg_attrconddefs() {
        return tgg_attrconddefs;
    }

    public void addTgg_attrconddef(Tgg_attrconddef tgg_attrconddef) {
        this.tgg_attrconddefs.add(tgg_attrconddef);
    }
    public tgg_TripleGraphGrammarFile getTgg_triplegraphgrammarfile() {
        return tgg_triplegraphgrammarfile;
    }

    public void setTgg_triplegraphgrammarfile(tgg_TripleGraphGrammarFile tgg_triplegraphgrammarfile) {
        this.tgg_triplegraphgrammarfile = tgg_triplegraphgrammarfile;
    }

}