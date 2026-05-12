





import java.util.List;
import java.util.ArrayList;

public class MDAIntermediateStateMachine_Content  {

    private String name;





    private List<MDAIntermediateStateMachine_Operation> mdaintermediatestatemachine_operations;


    public MDAIntermediateStateMachine_Content(
        String name    ) {
        this.name = name;
        this.mdaintermediatestatemachine_operations = new ArrayList<>();
    }

    public MDAIntermediateStateMachine_Content(
        String name        ArrayList<MDAIntermediateStateMachine_Operation> mdaintermediatestatemachine_operations    ) {
        this.name = name;
        this.mdaintermediatestatemachine_operations = mdaintermediatestatemachine_operations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<MDAIntermediateStateMachine_Operation> getMdaintermediatestatemachine_operations() {
        return mdaintermediatestatemachine_operations;
    }

    public void addMdaintermediatestatemachine_operation(Mdaintermediatestatemachine_operation mdaintermediatestatemachine_operation) {
        this.mdaintermediatestatemachine_operations.add(mdaintermediatestatemachine_operation);
    }

}