





import java.util.List;
import java.util.ArrayList;

public class uma_Task extends ContentElement, WorkDefinition {






    private uma_Discipline uma_discipline;




    private uma_Role uma_role;




    private uma_TaskDescriptor uma_taskdescriptor;




    private List<uma_Role> uma_roles;




    private List<uma_ToolMentor> uma_toolmentors;




    private List<uma_EstimationConsiderations> uma_estimationconsiderationss;


    public uma_Task(
    ) {
        super(
        );
        this.uma_roles = new ArrayList<>();
        this.uma_toolmentors = new ArrayList<>();
        this.uma_estimationconsiderationss = new ArrayList<>();
    }

    public uma_Task(
        ArrayList<uma_Role> uma_roles,        ArrayList<uma_ToolMentor> uma_toolmentors,        ArrayList<uma_EstimationConsiderations> uma_estimationconsiderationss    ) {
        this.uma_roles = uma_roles;
        this.uma_toolmentors = uma_toolmentors;
        this.uma_estimationconsiderationss = uma_estimationconsiderationss;
    }


    public uma_Discipline getUma_discipline() {
        return uma_discipline;
    }

    public void setUma_discipline(uma_Discipline uma_discipline) {
        this.uma_discipline = uma_discipline;
    }
    public uma_Role getUma_role() {
        return uma_role;
    }

    public void setUma_role(uma_Role uma_role) {
        this.uma_role = uma_role;
    }
    public uma_TaskDescriptor getUma_taskdescriptor() {
        return uma_taskdescriptor;
    }

    public void setUma_taskdescriptor(uma_TaskDescriptor uma_taskdescriptor) {
        this.uma_taskdescriptor = uma_taskdescriptor;
    }
    public List<uma_Role> getUma_roles() {
        return uma_roles;
    }

    public void addUma_role(Uma_role uma_role) {
        this.uma_roles.add(uma_role);
    }
    public List<uma_ToolMentor> getUma_toolmentors() {
        return uma_toolmentors;
    }

    public void addUma_toolmentor(Uma_toolmentor uma_toolmentor) {
        this.uma_toolmentors.add(uma_toolmentor);
    }
    public List<uma_EstimationConsiderations> getUma_estimationconsiderationss() {
        return uma_estimationconsiderationss;
    }

    public void addUma_estimationconsiderations(Uma_estimationconsiderations uma_estimationconsiderations) {
        this.uma_estimationconsiderationss.add(uma_estimationconsiderations);
    }

}