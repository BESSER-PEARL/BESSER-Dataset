





import java.util.List;
import java.util.ArrayList;

public class rcl_VarAssignment extends Statement {

    private String name;





    private rcl_RoverValue rcl_rovervalue;


    public rcl_VarAssignment(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rcl_RoverValue getRcl_rovervalue() {
        return rcl_rovervalue;
    }

    public void setRcl_rovervalue(rcl_RoverValue rcl_rovervalue) {
        this.rcl_rovervalue = rcl_rovervalue;
    }

}