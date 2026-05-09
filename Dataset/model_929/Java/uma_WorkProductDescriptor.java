





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProductDescriptor extends Descriptor {

    private String activityEntryState;
    private String activityExitState;





    private uma_WorkProduct uma_workproduct;




    private uma_TaskDescriptor uma_taskdescriptor;




    private uma_TaskDescriptor uma_taskdescriptor;




    private uma_WorkProductDescriptor uma_workproductdescriptor;




    private uma_TaskDescriptor uma_taskdescriptor;




    private uma_TaskDescriptor uma_taskdescriptor;




    private uma_WorkProductDescriptor uma_workproductdescriptor;




    private uma_ProcessComponentInterface uma_processcomponentinterface;




    private uma_RoleDescriptor uma_roledescriptor;




    private uma_RoleDescriptor uma_roledescriptor;




    private List<uma_WorkProductDescriptor> uma_workproductdescriptors;


    public uma_WorkProductDescriptor(
        String activityEntryState,        String activityExitState    ) {
        super(
        );
        this.activityEntryState = activityEntryState;
        this.activityExitState = activityExitState;
        this.uma_workproductdescriptors = new ArrayList<>();
    }

    public uma_WorkProductDescriptor(
        String activityEntryState,        String activityExitState        ArrayList<uma_WorkProductDescriptor> uma_workproductdescriptors    ) {
        this.activityEntryState = activityEntryState;
        this.activityExitState = activityExitState;
        this.uma_workproductdescriptors = uma_workproductdescriptors;
    }

    public String getActivityentrystate() {
        return activityEntryState;
    }

    public void setActivityentrystate(String activityEntryState) {
        this.activityEntryState = activityEntryState;
    }
    public String getActivityexitstate() {
        return activityExitState;
    }

    public void setActivityexitstate(String activityExitState) {
        this.activityExitState = activityExitState;
    }

    public uma_WorkProduct getUma_workproduct() {
        return uma_workproduct;
    }

    public void setUma_workproduct(uma_WorkProduct uma_workproduct) {
        this.uma_workproduct = uma_workproduct;
    }
    public uma_TaskDescriptor getUma_taskdescriptor() {
        return uma_taskdescriptor;
    }

    public void setUma_taskdescriptor(uma_TaskDescriptor uma_taskdescriptor) {
        this.uma_taskdescriptor = uma_taskdescriptor;
    }
    public uma_TaskDescriptor getUma_taskdescriptor() {
        return uma_taskdescriptor;
    }

    public void setUma_taskdescriptor(uma_TaskDescriptor uma_taskdescriptor) {
        this.uma_taskdescriptor = uma_taskdescriptor;
    }
    public uma_WorkProductDescriptor getUma_workproductdescriptor() {
        return uma_workproductdescriptor;
    }

    public void setUma_workproductdescriptor(uma_WorkProductDescriptor uma_workproductdescriptor) {
        this.uma_workproductdescriptor = uma_workproductdescriptor;
    }
    public uma_TaskDescriptor getUma_taskdescriptor() {
        return uma_taskdescriptor;
    }

    public void setUma_taskdescriptor(uma_TaskDescriptor uma_taskdescriptor) {
        this.uma_taskdescriptor = uma_taskdescriptor;
    }
    public uma_TaskDescriptor getUma_taskdescriptor() {
        return uma_taskdescriptor;
    }

    public void setUma_taskdescriptor(uma_TaskDescriptor uma_taskdescriptor) {
        this.uma_taskdescriptor = uma_taskdescriptor;
    }
    public uma_WorkProductDescriptor getUma_workproductdescriptor() {
        return uma_workproductdescriptor;
    }

    public void setUma_workproductdescriptor(uma_WorkProductDescriptor uma_workproductdescriptor) {
        this.uma_workproductdescriptor = uma_workproductdescriptor;
    }
    public uma_ProcessComponentInterface getUma_processcomponentinterface() {
        return uma_processcomponentinterface;
    }

    public void setUma_processcomponentinterface(uma_ProcessComponentInterface uma_processcomponentinterface) {
        this.uma_processcomponentinterface = uma_processcomponentinterface;
    }
    public uma_RoleDescriptor getUma_roledescriptor() {
        return uma_roledescriptor;
    }

    public void setUma_roledescriptor(uma_RoleDescriptor uma_roledescriptor) {
        this.uma_roledescriptor = uma_roledescriptor;
    }
    public uma_RoleDescriptor getUma_roledescriptor() {
        return uma_roledescriptor;
    }

    public void setUma_roledescriptor(uma_RoleDescriptor uma_roledescriptor) {
        this.uma_roledescriptor = uma_roledescriptor;
    }
    public List<uma_WorkProductDescriptor> getUma_workproductdescriptors() {
        return uma_workproductdescriptors;
    }

    public void addUma_workproductdescriptor(Uma_workproductdescriptor uma_workproductdescriptor) {
        this.uma_workproductdescriptors.add(uma_workproductdescriptor);
    }

}