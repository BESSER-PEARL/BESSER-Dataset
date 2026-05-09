





import java.util.List;
import java.util.ArrayList;

public class uma_Task extends WorkDefinition, ContentElement {






    private List<uma_WorkProduct> uma_workproducts;




    private List<uma_WorkProduct> uma_workproducts;




    private List<uma_Role> uma_roles;




    private List<uma_WorkProduct> uma_workproducts;




    private List<uma_EstimationConsiderations> uma_estimationconsiderationss;




    private List<uma_ToolMentor> uma_toolmentors;




    private List<uma_Role> uma_roles;


    public uma_Task(
    ) {
        super(
        );
        this.uma_workproducts = new ArrayList<>();
        this.uma_workproducts = new ArrayList<>();
        this.uma_roles = new ArrayList<>();
        this.uma_workproducts = new ArrayList<>();
        this.uma_estimationconsiderationss = new ArrayList<>();
        this.uma_toolmentors = new ArrayList<>();
        this.uma_roles = new ArrayList<>();
    }

    public uma_Task(
        ArrayList<uma_WorkProduct> uma_workproducts,        ArrayList<uma_WorkProduct> uma_workproducts,        ArrayList<uma_Role> uma_roles,        ArrayList<uma_WorkProduct> uma_workproducts,        ArrayList<uma_EstimationConsiderations> uma_estimationconsiderationss,        ArrayList<uma_ToolMentor> uma_toolmentors,        ArrayList<uma_Role> uma_roles    ) {
        this.uma_workproducts = uma_workproducts;
        this.uma_workproducts = uma_workproducts;
        this.uma_roles = uma_roles;
        this.uma_workproducts = uma_workproducts;
        this.uma_estimationconsiderationss = uma_estimationconsiderationss;
        this.uma_toolmentors = uma_toolmentors;
        this.uma_roles = uma_roles;
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
    public List<uma_EstimationConsiderations> getUma_estimationconsiderationss() {
        return uma_estimationconsiderationss;
    }

    public void addUma_estimationconsiderations(Uma_estimationconsiderations uma_estimationconsiderations) {
        this.uma_estimationconsiderationss.add(uma_estimationconsiderations);
    }
    public List<uma_ToolMentor> getUma_toolmentors() {
        return uma_toolmentors;
    }

    public void addUma_toolmentor(Uma_toolmentor uma_toolmentor) {
        this.uma_toolmentors.add(uma_toolmentor);
    }
    public List<uma_Role> getUma_roles() {
        return uma_roles;
    }

    public void addUma_role(Uma_role uma_role) {
        this.uma_roles.add(uma_role);
    }

}