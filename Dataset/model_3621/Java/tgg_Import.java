





import java.util.List;
import java.util.ArrayList;

public class tgg_Import  {

    private String name;





    private tgg_TripleGraphGrammarFile tgg_triplegraphgrammarfile;


    public tgg_Import(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tgg_TripleGraphGrammarFile getTgg_triplegraphgrammarfile() {
        return tgg_triplegraphgrammarfile;
    }

    public void setTgg_triplegraphgrammarfile(tgg_TripleGraphGrammarFile tgg_triplegraphgrammarfile) {
        this.tgg_triplegraphgrammarfile = tgg_triplegraphgrammarfile;
    }

}