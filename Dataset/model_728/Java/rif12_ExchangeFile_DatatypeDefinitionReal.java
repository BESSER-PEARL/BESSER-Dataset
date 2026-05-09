





import java.util.List;
import java.util.ArrayList;

public class rif12_ExchangeFile_DatatypeDefinitionReal extends DatatypeDefinitionSimple {

    private String max;
    private String min;
    private String accuracy;



    public rif12_ExchangeFile_DatatypeDefinitionReal(
        String max,        String min,        String accuracy    ) {
        super(
        );
        this.max = max;
        this.min = min;
        this.accuracy = accuracy;
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
    public String getAccuracy() {
        return accuracy;
    }

    public void setAccuracy(String accuracy) {
        this.accuracy = accuracy;
    }


}