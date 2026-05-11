





import java.util.List;
import java.util.ArrayList;

public class dsl_Race  {

    private String name;





    private dsl_Model dsl_model;




    private dsl_Unit dsl_unit;


    public dsl_Race(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Model getDsl_model() {
        return dsl_model;
    }

    public void setDsl_model(dsl_Model dsl_model) {
        this.dsl_model = dsl_model;
    }
    public dsl_Unit getDsl_unit() {
        return dsl_unit;
    }

    public void setDsl_unit(dsl_Unit dsl_unit) {
        this.dsl_unit = dsl_unit;
    }

}