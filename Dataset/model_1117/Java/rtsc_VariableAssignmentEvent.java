





import java.util.List;
import java.util.ArrayList;

public class rtsc_VariableAssignmentEvent extends Event {

    private String value;





    private rtsc_Variable rtsc_variable;


    public rtsc_VariableAssignmentEvent(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public rtsc_Variable getRtsc_variable() {
        return rtsc_variable;
    }

    public void setRtsc_variable(rtsc_Variable rtsc_variable) {
        this.rtsc_variable = rtsc_variable;
    }

}