





import java.util.List;
import java.util.ArrayList;

public class aml_Reliability  {

    private String description;
    private String ordinal;
    private String label;
    private String symbol;





    private aml_Evidence aml_evidence;




    private aml_DocumentRoot aml_documentroot;


    public aml_Reliability(
        String description,        String ordinal,        String label,        String symbol    ) {
        this.description = description;
        this.ordinal = ordinal;
        this.label = label;
        this.symbol = symbol;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(String ordinal) {
        this.ordinal = ordinal;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public aml_Evidence getAml_evidence() {
        return aml_evidence;
    }

    public void setAml_evidence(aml_Evidence aml_evidence) {
        this.aml_evidence = aml_evidence;
    }
    public aml_DocumentRoot getAml_documentroot() {
        return aml_documentroot;
    }

    public void setAml_documentroot(aml_DocumentRoot aml_documentroot) {
        this.aml_documentroot = aml_documentroot;
    }

}