





import java.util.List;
import java.util.ArrayList;

public class uma_ProcessComponentInterface extends BreakdownElement {

    private String group2;





    private List<uma_TaskDescriptor> uma_taskdescriptors;


    public uma_ProcessComponentInterface(
        String group2    ) {
        super(
        );
        this.group2 = group2;
        this.uma_taskdescriptors = new ArrayList<>();
    }

    public uma_ProcessComponentInterface(
        String group2        ArrayList<uma_TaskDescriptor> uma_taskdescriptors    ) {
        this.group2 = group2;
        this.uma_taskdescriptors = uma_taskdescriptors;
    }

    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }

    public List<uma_TaskDescriptor> getUma_taskdescriptors() {
        return uma_taskdescriptors;
    }

    public void addUma_taskdescriptor(Uma_taskdescriptor uma_taskdescriptor) {
        this.uma_taskdescriptors.add(uma_taskdescriptor);
    }

}