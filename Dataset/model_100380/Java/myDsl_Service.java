





import java.util.List;
import java.util.ArrayList;

public class myDsl_Service  {

    private String name;





    private myDsl_Statemachine mydsl_statemachine;


    public myDsl_Service(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_Statemachine getMydsl_statemachine() {
        return mydsl_statemachine;
    }

    public void setMydsl_statemachine(myDsl_Statemachine mydsl_statemachine) {
        this.mydsl_statemachine = mydsl_statemachine;
    }

}