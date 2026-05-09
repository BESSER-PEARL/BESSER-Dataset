





import java.util.List;
import java.util.ArrayList;

public class uma_Task extends ContentElement, WorkDefinition {






    private List<uma_Role> uma_roles;




    private List<uma_Role> uma_roles;




    private List<uma_WorkProduct> uma_workproducts;




    private List<uma_WorkProduct> uma_workproducts;




    private List<uma_WorkProduct> uma_workproducts;




    private uma_TaskDescriptor uma_taskdescriptor;


    public uma_Task(
    ) {
        super(
        );
        this.uma_roles = new ArrayList<>();
        this.uma_roles = new ArrayList<>();
        this.uma_workproducts = new ArrayList<>();
        this.uma_workproducts = new ArrayList<>();
        this.uma_workproducts = new ArrayList<>();
    }

    public uma_Task(
        ArrayList<uma_Role> uma_roles,        ArrayList<uma_Role> uma_roles,        ArrayList<uma_WorkProduct> uma_workproducts,        ArrayList<uma_WorkProduct> uma_workproducts,        ArrayList<uma_WorkProduct> uma_workproducts    ) {
        this.uma_roles = uma_roles;
        this.uma_roles = uma_roles;
        this.uma_workproducts = uma_workproducts;
        this.uma_workproducts = uma_workproducts;
        this.uma_workproducts = uma_workproducts;
    }


    public List<uma_Role> getUma_roles() {
        return uma_roles;
    }

    public void addUma_role(Uma_role uma_role) {
        this.uma_roles.add(uma_role);
    }
    public List<uma_Role> getUma_roles() {
        return uma_roles;
    }

    public void addUma_role(Uma_role uma_role) {
        this.uma_roles.add(uma_role);
    }
    public List<uma_WorkProduct> getUma_workproducts() {
        return uma_workproducts;
    }

    public void addUma_workproduct(Uma_workproduct uma_workproduct) {
        this.uma_workproducts.add(uma_workproduct);
    }
    public List<uma_WorkProduct> getUma_workproducts() {
        return uma_workproducts;
    }

    public void addUma_workproduct(Uma_workproduct uma_workproduct) {
        this.uma_workproducts.add(uma_workproduct);
    }
    public List<uma_WorkProduct> getUma_workproducts() {
        return uma_workproducts;
    }

    public void addUma_workproduct(Uma_workproduct uma_workproduct) {
        this.uma_workproducts.add(uma_workproduct);
    }
    public uma_TaskDescriptor getUma_taskdescriptor() {
        return uma_taskdescriptor;
    }

    public void setUma_taskdescriptor(uma_TaskDescriptor uma_taskdescriptor) {
        this.uma_taskdescriptor = uma_taskdescriptor;
    }

}