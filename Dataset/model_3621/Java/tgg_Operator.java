





import java.util.List;
import java.util.ArrayList;

public class tgg_Operator  {

    private String value;





    private tgg_OperatorPattern tgg_operatorpattern;


    public tgg_Operator(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public tgg_OperatorPattern getTgg_operatorpattern() {
        return tgg_operatorpattern;
    }

    public void setTgg_operatorpattern(tgg_OperatorPattern tgg_operatorpattern) {
        this.tgg_operatorpattern = tgg_operatorpattern;
    }

}