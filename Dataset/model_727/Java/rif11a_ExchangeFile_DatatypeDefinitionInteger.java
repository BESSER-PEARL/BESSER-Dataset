





import java.util.List;
import java.util.ArrayList;

public class rif11a_ExchangeFile_DatatypeDefinitionInteger extends DatatypeDefinitionSimple {

    private String max;
    private String min;



    public rif11a_ExchangeFile_DatatypeDefinitionInteger(
        String max,        String min    ) {
        super(
        );
        this.max = max;
        this.min = min;
    }


    public String getMax() {
        return max;
    }

    public void setMax(String max) {
        this.max = max;
    }
    public String getMin() {
        return min;
    }

    public void setMin(String min) {
        this.min = min;
    }


}