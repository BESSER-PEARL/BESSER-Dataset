





import java.util.List;
import java.util.ArrayList;

public class aml_Parameter  {

    private String symbol;





    private aml_AggregationRule aml_aggregationrule;


    public aml_Parameter(
        String symbol    ) {
        this.symbol = symbol;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public aml_AggregationRule getAml_aggregationrule() {
        return aml_aggregationrule;
    }

    public void setAml_aggregationrule(aml_AggregationRule aml_aggregationrule) {
        this.aml_aggregationrule = aml_aggregationrule;
    }

}