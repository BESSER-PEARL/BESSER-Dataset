





import java.util.List;
import java.util.ArrayList;

public class uma_ProcessComponentInterface extends BreakdownElement {






    private uma_ProcessComponent uma_processcomponent;




    private List<uma_TaskDescriptor> uma_taskdescriptors;


    public uma_ProcessComponentInterface(
    ) {
        super(
        );
        this.uma_taskdescriptors = new ArrayList<>();
    }

    public uma_ProcessComponentInterface(
        ArrayList<uma_TaskDescriptor> uma_taskdescriptors    ) {
        this.uma_taskdescriptors = uma_taskdescriptors;
    }


    public uma_ProcessComponent getUma_processcomponent() {
        return uma_processcomponent;
    }

    public void setUma_processcomponent(uma_ProcessComponent uma_processcomponent) {
        this.uma_processcomponent = uma_processcomponent;
    }
    public List<uma_TaskDescriptor> getUma_taskdescriptors() {
        return uma_taskdescriptors;
    }

    public void addUma_taskdescriptor(Uma_taskdescriptor uma_taskdescriptor) {
        this.uma_taskdescriptors.add(uma_taskdescriptor);
    }

}