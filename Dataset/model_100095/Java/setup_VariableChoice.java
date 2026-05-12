





import java.util.List;
import java.util.ArrayList;

public class setup_VariableChoice  {

    private String value;
    private String label;





    private setup_ContextVariableTask setup_contextvariabletask;


    public setup_VariableChoice(
        String value,        String label    ) {
        this.value = value;
        this.label = label;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public setup_ContextVariableTask getSetup_contextvariabletask() {
        return setup_contextvariabletask;
    }

    public void setSetup_contextvariabletask(setup_ContextVariableTask setup_contextvariabletask) {
        this.setup_contextvariabletask = setup_contextvariabletask;
    }

}