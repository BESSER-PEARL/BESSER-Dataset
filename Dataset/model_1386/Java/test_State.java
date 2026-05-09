





import java.util.List;
import java.util.ArrayList;

public class test_State extends NamedElement {

    private String kind;





    private test_StateMachine test_statemachine;


    public test_State(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public test_StateMachine getTest_statemachine() {
        return test_statemachine;
    }

    public void setTest_statemachine(test_StateMachine test_statemachine) {
        this.test_statemachine = test_statemachine;
    }

}