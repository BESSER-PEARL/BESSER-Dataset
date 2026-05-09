





import java.util.List;
import java.util.ArrayList;

public class rtsc_Variable extends NamedElement {

    private String initialValue;
    private String runtimeValue;





    private rtsc_VariableAssignmentEvent rtsc_variableassignmentevent;


    public rtsc_Variable(
        String initialValue,        String runtimeValue    ) {
        super(
        );
        this.initialValue = initialValue;
        this.runtimeValue = runtimeValue;
    }


    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }
    public String getRuntimevalue() {
        return runtimeValue;
    }

    public void setRuntimevalue(String runtimeValue) {
        this.runtimeValue = runtimeValue;
    }

    public rtsc_VariableAssignmentEvent getRtsc_variableassignmentevent() {
        return rtsc_variableassignmentevent;
    }

    public void setRtsc_variableassignmentevent(rtsc_VariableAssignmentEvent rtsc_variableassignmentevent) {
        this.rtsc_variableassignmentevent = rtsc_variableassignmentevent;
    }

}