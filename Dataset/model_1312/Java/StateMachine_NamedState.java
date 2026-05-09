





import java.util.List;
import java.util.ArrayList;

public class StateMachine_NamedState extends State {

    private String name;



    public StateMachine_NamedState(
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