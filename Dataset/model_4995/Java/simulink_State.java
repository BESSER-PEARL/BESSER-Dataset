





import java.util.List;
import java.util.ArrayList;

public class simulink_State extends CompositeStateflowElement, Vertex {

    private int executionOrder;
    private String decomposition;



    public simulink_State(
        int executionOrder,        String decomposition    ) {
        super(
        );
        this.executionOrder = executionOrder;
        this.decomposition = decomposition;
    }


    public int getExecutionorder() {
        return executionOrder;
    }

    public void setExecutionorder(int executionOrder) {
        this.executionOrder = executionOrder;
    }
    public String getDecomposition() {
        return decomposition;
    }

    public void setDecomposition(String decomposition) {
        this.decomposition = decomposition;
    }


}