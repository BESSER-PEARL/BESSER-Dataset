





import java.util.List;
import java.util.ArrayList;

public class rtsc_Guard  {

    private String value;





    private rtsc_Transition rtsc_transition;




    private rtsc_Variable rtsc_variable;


    public rtsc_Guard(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public rtsc_Transition getRtsc_transition() {
        return rtsc_transition;
    }

    public void setRtsc_transition(rtsc_Transition rtsc_transition) {
        this.rtsc_transition = rtsc_transition;
    }
    public rtsc_Variable getRtsc_variable() {
        return rtsc_variable;
    }

    public void setRtsc_variable(rtsc_Variable rtsc_variable) {
        this.rtsc_variable = rtsc_variable;
    }

}