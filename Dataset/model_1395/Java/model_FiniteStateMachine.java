





import java.util.List;
import java.util.ArrayList;

public class model_FiniteStateMachine extends AbstractState {






    private model_AbstractState model_abstractstate;




    private List<model_AbstractState> model_abstractstates;




    private model_AbstractState model_abstractstate;


    public model_FiniteStateMachine(
    ) {
        super(
        );
        this.model_abstractstates = new ArrayList<>();
    }

    public model_FiniteStateMachine(
        ArrayList<model_AbstractState> model_abstractstates    ) {
        this.model_abstractstates = model_abstractstates;
    }


    public model_AbstractState getModel_abstractstate() {
        return model_abstractstate;
    }

    public void setModel_abstractstate(model_AbstractState model_abstractstate) {
        this.model_abstractstate = model_abstractstate;
    }
    public List<model_AbstractState> getModel_abstractstates() {
        return model_abstractstates;
    }

    public void addModel_abstractstate(Model_abstractstate model_abstractstate) {
        this.model_abstractstates.add(model_abstractstate);
    }
    public model_AbstractState getModel_abstractstate() {
        return model_abstractstate;
    }

    public void setModel_abstractstate(model_AbstractState model_abstractstate) {
        this.model_abstractstate = model_abstractstate;
    }

}