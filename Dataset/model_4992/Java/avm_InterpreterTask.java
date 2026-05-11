





import java.util.List;
import java.util.ArrayList;

public class avm_InterpreterTask extends WorkflowTaskBase {

    private String COMName;
    private String Parameters;



    public avm_InterpreterTask(
        String COMName,        String Parameters    ) {
        super(
        );
        this.COMName = COMName;
        this.Parameters = Parameters;
    }


    public String getComname() {
        return COMName;
    }

    public void setComname(String COMName) {
        this.COMName = COMName;
    }
    public String getParameters() {
        return Parameters;
    }

    public void setParameters(String Parameters) {
        this.Parameters = Parameters;
    }


}