





import java.util.List;
import java.util.ArrayList;

public class myDsl_Event  {

    private boolean resetEvent;
    private String name;





    private myDsl_Statemachine mydsl_statemachine;


    public myDsl_Event(
        boolean resetEvent,        String name    ) {
        this.resetEvent = resetEvent;
        this.name = name;
    }


    public boolean getResetevent() {
        return resetEvent;
    }

    public void setResetevent(boolean resetEvent) {
        this.resetEvent = resetEvent;
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