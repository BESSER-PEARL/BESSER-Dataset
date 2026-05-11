





import java.util.List;
import java.util.ArrayList;

public class optGrammar_ImportDirective  {

    private String importURI;
    private String unitAlias;





    private optGrammar_Model optgrammar_model;


    public optGrammar_ImportDirective(
        String importURI,        String unitAlias    ) {
        this.importURI = importURI;
        this.unitAlias = unitAlias;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }
    public String getUnitalias() {
        return unitAlias;
    }

    public void setUnitalias(String unitAlias) {
        this.unitAlias = unitAlias;
    }

    public optGrammar_Model getOptgrammar_model() {
        return optgrammar_model;
    }

    public void setOptgrammar_model(optGrammar_Model optgrammar_model) {
        this.optgrammar_model = optgrammar_model;
    }

}