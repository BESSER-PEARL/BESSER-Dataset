





import java.util.List;
import java.util.ArrayList;

public class stateMachine_StateTransition extends AbstractMachineElement {

    private String visibility;



    public stateMachine_StateTransition(
        String visibility    ) {
        super(
        );
        this.visibility = visibility;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}