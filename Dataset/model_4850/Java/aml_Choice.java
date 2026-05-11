





import java.util.List;
import java.util.ArrayList;

public class aml_Choice  {

    private String symbol;
    private String description;
    private String label;
    private String ordinal;



    public aml_Choice(
        String symbol,        String description,        String label,        String ordinal    ) {
        this.symbol = symbol;
        this.description = description;
        this.label = label;
        this.ordinal = ordinal;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(String ordinal) {
        this.ordinal = ordinal;
    }


}