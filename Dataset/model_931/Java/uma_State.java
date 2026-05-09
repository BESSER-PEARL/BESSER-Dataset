





import java.util.List;
import java.util.ArrayList;

public class uma_State extends Vertex {






    private List<uma_WorkProduct> uma_workproducts;




    private uma_StateMachine uma_statemachine;


    public uma_State(
    ) {
        super(
        );
        this.uma_workproducts = new ArrayList<>();
    }

    public uma_State(
        ArrayList<uma_WorkProduct> uma_workproducts    ) {
        this.uma_workproducts = uma_workproducts;
    }


    public List<uma_WorkProduct> getUma_workproducts() {
        return uma_workproducts;
    }

    public void addUma_workproduct(Uma_workproduct uma_workproduct) {
        this.uma_workproducts.add(uma_workproduct);
    }
    public uma_StateMachine getUma_statemachine() {
        return uma_statemachine;
    }

    public void setUma_statemachine(uma_StateMachine uma_statemachine) {
        this.uma_statemachine = uma_statemachine;
    }

}