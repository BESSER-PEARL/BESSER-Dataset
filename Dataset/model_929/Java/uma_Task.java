





import java.util.List;
import java.util.ArrayList;

public class uma_Task extends WorkDefinition, ContentElement {






    private List<uma_WorkProduct> uma_workproducts;




    private List<uma_Role> uma_roles;




    private List<uma_WorkProduct> uma_workproducts;




    private uma_Role uma_role;




    private List<uma_WorkProduct> uma_workproducts;


    public uma_Task(
    ) {
        super(
        );
        this.uma_workproducts = new ArrayList<>();
        this.uma_roles = new ArrayList<>();
        this.uma_workproducts = new ArrayList<>();
        this.uma_workproducts = new ArrayList<>();
    }

    public uma_Task(
        ArrayList<uma_WorkProduct> uma_workproducts,        ArrayList<uma_Role> uma_roles,        ArrayList<uma_WorkProduct> uma_workproducts,        ArrayList<uma_WorkProduct> uma_workproducts    ) {
        this.uma_workproducts = uma_workproducts;
        this.uma_roles = uma_roles;
        this.uma_workproducts = uma_workproducts;
        this.uma_workproducts = uma_workproducts;
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
    public uma_Role getUma_role() {
        return uma_role;
    }

    public void setUma_role(uma_Role uma_role) {
        this.uma_role = uma_role;
    }
    public List<uma_WorkProduct> getUma_workproducts() {
        return uma_workproducts;
    }

    public void addUma_workproduct(Uma_workproduct uma_workproduct) {
        this.uma_workproducts.add(uma_workproduct);
    }

}