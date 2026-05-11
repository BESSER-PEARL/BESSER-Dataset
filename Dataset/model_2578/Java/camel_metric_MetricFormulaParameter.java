





import java.util.List;
import java.util.ArrayList;

public class camel_metric_MetricFormulaParameter  {

    private String name;





    private SingleValue singlevalue;


    public camel_metric_MetricFormulaParameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SingleValue getSinglevalue() {
        return singlevalue;
    }

    public void setSinglevalue(SingleValue singlevalue) {
        this.singlevalue = singlevalue;
    }

}