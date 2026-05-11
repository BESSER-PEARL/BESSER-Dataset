





import java.util.List;
import java.util.ArrayList;

public class dSL_EndWhen  {

    private int times;
    private String name;





    private dSL_EndCondition dsl_endcondition;


    public dSL_EndWhen(
        int times,        String name    ) {
        this.times = times;
        this.name = name;
    }


    public int getTimes() {
        return times;
    }

    public void setTimes(int times) {
        this.times = times;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dSL_EndCondition getDsl_endcondition() {
        return dsl_endcondition;
    }

    public void setDsl_endcondition(dSL_EndCondition dsl_endcondition) {
        this.dsl_endcondition = dsl_endcondition;
    }

}