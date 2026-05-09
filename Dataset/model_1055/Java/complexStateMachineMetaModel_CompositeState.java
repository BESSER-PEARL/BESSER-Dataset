





import java.util.List;
import java.util.ArrayList;

public class complexStateMachineMetaModel_CompositeState extends State {






    private complexStateMachineMetaModel_State complexstatemachinemetamodel_state;




    private List<complexStateMachineMetaModel_State> complexstatemachinemetamodel_states;




    private complexStateMachineMetaModel_State complexstatemachinemetamodel_state;


    public complexStateMachineMetaModel_CompositeState(
    ) {
        super(
        );
        this.complexstatemachinemetamodel_states = new ArrayList<>();
    }

    public complexStateMachineMetaModel_CompositeState(
        ArrayList<complexStateMachineMetaModel_State> complexstatemachinemetamodel_states    ) {
        this.complexstatemachinemetamodel_states = complexstatemachinemetamodel_states;
    }


    public complexStateMachineMetaModel_State getComplexstatemachinemetamodel_state() {
        return complexstatemachinemetamodel_state;
    }

    public void setComplexstatemachinemetamodel_state(complexStateMachineMetaModel_State complexstatemachinemetamodel_state) {
        this.complexstatemachinemetamodel_state = complexstatemachinemetamodel_state;
    }
    public List<complexStateMachineMetaModel_State> getComplexstatemachinemetamodel_states() {
        return complexstatemachinemetamodel_states;
    }

    public void addComplexstatemachinemetamodel_state(Complexstatemachinemetamodel_state complexstatemachinemetamodel_state) {
        this.complexstatemachinemetamodel_states.add(complexstatemachinemetamodel_state);
    }
    public complexStateMachineMetaModel_State getComplexstatemachinemetamodel_state() {
        return complexstatemachinemetamodel_state;
    }

    public void setComplexstatemachinemetamodel_state(complexStateMachineMetaModel_State complexstatemachinemetamodel_state) {
        this.complexstatemachinemetamodel_state = complexstatemachinemetamodel_state;
    }

}