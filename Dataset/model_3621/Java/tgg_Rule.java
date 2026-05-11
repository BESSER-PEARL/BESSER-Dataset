





import java.util.List;
import java.util.ArrayList;

public class tgg_Rule extends NamedElements {

    private boolean abstractRule;





    private tgg_TripleGraphGrammarFile tgg_triplegraphgrammarfile;




    private tgg_Schema tgg_schema;




    private tgg_Rule tgg_rule;


    public tgg_Rule(
        boolean abstractRule    ) {
        super(
        );
        this.abstractRule = abstractRule;
    }


    public boolean getAbstractrule() {
        return abstractRule;
    }

    public void setAbstractrule(boolean abstractRule) {
        this.abstractRule = abstractRule;
    }

    public tgg_TripleGraphGrammarFile getTgg_triplegraphgrammarfile() {
        return tgg_triplegraphgrammarfile;
    }

    public void setTgg_triplegraphgrammarfile(tgg_TripleGraphGrammarFile tgg_triplegraphgrammarfile) {
        this.tgg_triplegraphgrammarfile = tgg_triplegraphgrammarfile;
    }
    public tgg_Schema getTgg_schema() {
        return tgg_schema;
    }

    public void setTgg_schema(tgg_Schema tgg_schema) {
        this.tgg_schema = tgg_schema;
    }
    public tgg_Rule getTgg_rule() {
        return tgg_rule;
    }

    public void setTgg_rule(tgg_Rule tgg_rule) {
        this.tgg_rule = tgg_rule;
    }

}