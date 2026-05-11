





import java.util.List;
import java.util.ArrayList;

public class tgg_Using  {

    private String importedNamespace;





    private tgg_TripleGraphGrammarFile tgg_triplegraphgrammarfile;


    public tgg_Using(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public tgg_TripleGraphGrammarFile getTgg_triplegraphgrammarfile() {
        return tgg_triplegraphgrammarfile;
    }

    public void setTgg_triplegraphgrammarfile(tgg_TripleGraphGrammarFile tgg_triplegraphgrammarfile) {
        this.tgg_triplegraphgrammarfile = tgg_triplegraphgrammarfile;
    }

}