





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_ETF  {

    private String id;
    private String precentage;





    private Class_Diagram_for_Proposed_system_LeavesAllocated class_diagram_for_proposed_system_leavesallocated;


    public Class_Diagram_for_Proposed_system_ETF(
        String id,        String precentage    ) {
        this.id = id;
        this.precentage = precentage;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPrecentage() {
        return precentage;
    }

    public void setPrecentage(String precentage) {
        this.precentage = precentage;
    }

    public Class_Diagram_for_Proposed_system_LeavesAllocated getClass_diagram_for_proposed_system_leavesallocated() {
        return class_diagram_for_proposed_system_leavesallocated;
    }

    public void setClass_diagram_for_proposed_system_leavesallocated(Class_Diagram_for_Proposed_system_LeavesAllocated class_diagram_for_proposed_system_leavesallocated) {
        this.class_diagram_for_proposed_system_leavesallocated = class_diagram_for_proposed_system_leavesallocated;
    }

}