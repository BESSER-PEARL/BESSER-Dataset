





import java.util.List;
import java.util.ArrayList;

public class dsl_IDevice  {

    private String typeof;
    private String name;





    private dsl_Robot dsl_robot;


    public dsl_IDevice(
        String typeof,        String name    ) {
        this.typeof = typeof;
        this.name = name;
    }


    public String getTypeof() {
        return typeof;
    }

    public void setTypeof(String typeof) {
        this.typeof = typeof;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Robot getDsl_robot() {
        return dsl_robot;
    }

    public void setDsl_robot(dsl_Robot dsl_robot) {
        this.dsl_robot = dsl_robot;
    }

}