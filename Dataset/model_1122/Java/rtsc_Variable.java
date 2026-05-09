





import java.util.List;
import java.util.ArrayList;

public class rtsc_Variable extends NamedElement {

    private String initialValue;





    private rtsc_VariableAssignmentEvent rtsc_variableassignmentevent;




    private rtsc_Realtimestatechart rtsc_realtimestatechart;




    private rtsc_Realtimestatechart rtsc_realtimestatechart;


    public rtsc_Variable(
        String initialValue    ) {
        super(
        );
        this.initialValue = initialValue;
    }


    public String getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(String initialValue) {
        this.initialValue = initialValue;
    }

    public rtsc_VariableAssignmentEvent getRtsc_variableassignmentevent() {
        return rtsc_variableassignmentevent;
    }

    public void setRtsc_variableassignmentevent(rtsc_VariableAssignmentEvent rtsc_variableassignmentevent) {
        this.rtsc_variableassignmentevent = rtsc_variableassignmentevent;
    }
    public rtsc_Realtimestatechart getRtsc_realtimestatechart() {
        return rtsc_realtimestatechart;
    }

    public void setRtsc_realtimestatechart(rtsc_Realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatechart = rtsc_realtimestatechart;
    }
    public rtsc_Realtimestatechart getRtsc_realtimestatechart() {
        return rtsc_realtimestatechart;
    }

    public void setRtsc_realtimestatechart(rtsc_Realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatechart = rtsc_realtimestatechart;
    }

}