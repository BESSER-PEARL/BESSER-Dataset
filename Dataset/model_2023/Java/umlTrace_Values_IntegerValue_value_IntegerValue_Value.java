





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Values_IntegerValue_value_IntegerValue_Value  {

    private int value_IntegerValue;





    private List<Values_umlTrace_State> values_umltrace_states;


    public umlTrace_Values_IntegerValue_value_IntegerValue_Value(
        int value_IntegerValue    ) {
        this.value_IntegerValue = value_IntegerValue;
        this.values_umltrace_states = new ArrayList<>();
    }

    public umlTrace_Values_IntegerValue_value_IntegerValue_Value(
        int value_IntegerValue        ArrayList<Values_umlTrace_State> values_umltrace_states    ) {
        this.value_IntegerValue = value_IntegerValue;
        this.values_umltrace_states = values_umltrace_states;
    }

    public int getValue_integervalue() {
        return value_IntegerValue;
    }

    public void setValue_integervalue(int value_IntegerValue) {
        this.value_IntegerValue = value_IntegerValue;
    }

    public List<Values_umlTrace_State> getValues_umltrace_states() {
        return values_umltrace_states;
    }

    public void addValues_umltrace_state(Values_umltrace_state values_umltrace_state) {
        this.values_umltrace_states.add(values_umltrace_state);
    }

}