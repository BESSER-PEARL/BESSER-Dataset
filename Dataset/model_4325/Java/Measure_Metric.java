





import java.util.List;
import java.util.ArrayList;

public class Measure_Metric  {

    private String desc;
    private String preferredValue;
    private String name;





    private Measure_Category measure_category;




    private Measure_Category measure_category;


    public Measure_Metric(
        String desc,        String preferredValue,        String name    ) {
        this.desc = desc;
        this.preferredValue = preferredValue;
        this.name = name;
    }


    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }
    public String getPreferredvalue() {
        return preferredValue;
    }

    public void setPreferredvalue(String preferredValue) {
        this.preferredValue = preferredValue;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Measure_Category getMeasure_category() {
        return measure_category;
    }

    public void setMeasure_category(Measure_Category measure_category) {
        this.measure_category = measure_category;
    }
    public Measure_Category getMeasure_category() {
        return measure_category;
    }

    public void setMeasure_category(Measure_Category measure_category) {
        this.measure_category = measure_category;
    }

}