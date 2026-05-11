





import java.util.List;
import java.util.ArrayList;

public class aml_Interval  {

    private String max;
    private String min;





    private aml_DocumentRoot aml_documentroot;


    public aml_Interval(
        String max,        String min    ) {
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

    public aml_DocumentRoot getAml_documentroot() {
        return aml_documentroot;
    }

    public void setAml_documentroot(aml_DocumentRoot aml_documentroot) {
        this.aml_documentroot = aml_documentroot;
    }

}