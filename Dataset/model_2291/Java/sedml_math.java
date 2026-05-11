





import java.util.List;
import java.util.ArrayList;

public class sedml_math  {

    private String xlms;





    private sedml_dataGenerator sedml_datagenerator;


    public sedml_math(
        String xlms    ) {
        this.xlms = xlms;
    }


    public String getXlms() {
        return xlms;
    }

    public void setXlms(String xlms) {
        this.xlms = xlms;
    }

    public sedml_dataGenerator getSedml_datagenerator() {
        return sedml_datagenerator;
    }

    public void setSedml_datagenerator(sedml_dataGenerator sedml_datagenerator) {
        this.sedml_datagenerator = sedml_datagenerator;
    }

}