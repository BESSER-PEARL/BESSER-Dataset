





import java.util.List;
import java.util.ArrayList;

public class vmlogo_Variable  {

    private String name;
    private float value;





    private vmlogo_StackFrame vmlogo_stackframe;


    public vmlogo_Variable(
        String name,        float value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }

    public vmlogo_StackFrame getVmlogo_stackframe() {
        return vmlogo_stackframe;
    }

    public void setVmlogo_stackframe(vmlogo_StackFrame vmlogo_stackframe) {
        this.vmlogo_stackframe = vmlogo_stackframe;
    }

}