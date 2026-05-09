





import java.util.List;
import java.util.ArrayList;

public class rtsc_Guard  {

    private boolean value;





    private rtsc_Variable rtsc_variable;




    private rtsc_Transition rtsc_transition;


    public rtsc_Guard(
        boolean value    ) {
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }

    public rtsc_Variable getRtsc_variable() {
        return rtsc_variable;
    }

    public void setRtsc_variable(rtsc_Variable rtsc_variable) {
        this.rtsc_variable = rtsc_variable;
    }
    public rtsc_Transition getRtsc_transition() {
        return rtsc_transition;
    }

    public void setRtsc_transition(rtsc_Transition rtsc_transition) {
        this.rtsc_transition = rtsc_transition;
    }

}