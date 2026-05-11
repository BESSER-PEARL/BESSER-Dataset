





import java.util.List;
import java.util.ArrayList;

public class kmLogo_Variable  {

    private float value;
    private String name;





    private kmLogo_StackFrame kmlogo_stackframe;


    public kmLogo_Variable(
        float value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public kmLogo_StackFrame getKmlogo_stackframe() {
        return kmlogo_stackframe;
    }

    public void setKmlogo_stackframe(kmLogo_StackFrame kmlogo_stackframe) {
        this.kmlogo_stackframe = kmlogo_stackframe;
    }

}