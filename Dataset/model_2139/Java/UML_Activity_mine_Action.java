





import java.util.List;
import java.util.ArrayList;

public class UML_Activity_mine_Action extends ActivityNode {

    private String outputs;
    private String inputs;



    public UML_Activity_mine_Action(
        String outputs,        String inputs    ) {
        super(
        );
        this.outputs = outputs;
        this.inputs = inputs;
    }


    public String getOutputs() {
        return outputs;
    }

    public void setOutputs(String outputs) {
        this.outputs = outputs;
    }
    public String getInputs() {
        return inputs;
    }

    public void setInputs(String inputs) {
        this.inputs = inputs;
    }


}