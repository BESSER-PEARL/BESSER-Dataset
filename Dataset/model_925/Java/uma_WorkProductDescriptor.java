





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProductDescriptor extends Descriptor {

    private String activityExitState;
    private String activityEntryState;





    private uma_WorkProductDescriptor uma_workproductdescriptor;




    private uma_TaskDescriptor uma_taskdescriptor;




    private uma_TaskDescriptor uma_taskdescriptor;




    private uma_WorkProduct uma_workproduct;




    private uma_TaskDescriptor uma_taskdescriptor;




    private uma_Milestone uma_milestone;




    private List<uma_WorkProductDescriptor> uma_workproductdescriptors;




    private uma_TaskDescriptor uma_taskdescriptor;




    private uma_WorkProductDescriptor uma_workproductdescriptor;




    private uma_ProcessComponentInterface uma_processcomponentinterface;


    public uma_WorkProductDescriptor(
        String activityExitState,        String activityEntryState    ) {
        super(
        );
        this.activityExitState = activityExitState;
        this.activityEntryState = activityEntryState;
        this.uma_workproductdescriptors = new ArrayList<>();
    }

    public uma_WorkProductDescriptor(
        String activityExitState,        String activityEntryState        ArrayList<uma_WorkProductDescriptor> uma_workproductdescriptors    ) {
        this.activityExitState = activityExitState;
        this.activityEntryState = activityEntryState;
        this.uma_workproductdescriptors = uma_workproductdescriptors;
    }

    public String getActivityexitstate() {
        return activityExitState;
    }

    public void setActivityexitstate(String activityExitState) {
        this.activityExitState = activityExitState;
    }
    public String getActivityentrystate() {
        return activityEntryState;
    }

    public void setActivityentrystate(String activityEntryState) {
        this.activityEntryState = activityEntryState;
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
    public uma_Milestone getUma_milestone() {
        return uma_milestone;
    }

    public void setUma_milestone(uma_Milestone uma_milestone) {
        this.uma_milestone = uma_milestone;
    }
    public List<uma_WorkProductDescriptor> getUma_workproductdescriptors() {
        return uma_workproductdescriptors;
    }

    public void addUma_workproductdescriptor(Uma_workproductdescriptor uma_workproductdescriptor) {
        this.uma_workproductdescriptors.add(uma_workproductdescriptor);
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

}