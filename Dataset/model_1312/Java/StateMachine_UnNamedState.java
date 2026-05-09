





import java.util.List;
import java.util.ArrayList;

public class StateMachine_UnNamedState extends State {

    private String name;



    public StateMachine_UnNamedState(
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