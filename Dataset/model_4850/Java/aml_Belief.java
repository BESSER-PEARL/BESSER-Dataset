





import java.util.List;
import java.util.ArrayList;

public class aml_Belief  {

    private String label;
    private String symbol;
    private String ordinal;
    private String description;



    public aml_Belief(
        String label,        String symbol,        String ordinal,        String description    ) {
        this.label = label;
        this.symbol = symbol;
        this.ordinal = ordinal;
        this.description = description;
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
    public String getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(String ordinal) {
        this.ordinal = ordinal;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}