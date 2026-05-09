





import java.util.List;
import java.util.ArrayList;

public class StateMachine_StateMachine extends Behavior {

    private String name;



    public StateMachine_StateMachine(
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


}