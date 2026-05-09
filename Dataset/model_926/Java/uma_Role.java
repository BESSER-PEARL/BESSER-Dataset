





import java.util.List;
import java.util.ArrayList;

public class uma_Role extends ContentElement, FulfillableElement {






    private uma_RoleDescriptor uma_roledescriptor;




    private List<uma_WorkProduct> uma_workproducts;




    private List<uma_WorkProduct> uma_workproducts;




    private uma_CompositeRole uma_compositerole;


    public uma_Role(
    ) {
        super(
        );
        this.uma_workproducts = new ArrayList<>();
        this.uma_workproducts = new ArrayList<>();
    }

    public uma_Role(
        ArrayList<uma_WorkProduct> uma_workproducts,        ArrayList<uma_WorkProduct> uma_workproducts    ) {
        this.uma_workproducts = uma_workproducts;
        this.uma_workproducts = uma_workproducts;
    }


    public uma_RoleDescriptor getUma_roledescriptor() {
        return uma_roledescriptor;
    }

    public void setUma_roledescriptor(uma_RoleDescriptor uma_roledescriptor) {
        this.uma_roledescriptor = uma_roledescriptor;
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
    public uma_CompositeRole getUma_compositerole() {
        return uma_compositerole;
    }

    public void setUma_compositerole(uma_CompositeRole uma_compositerole) {
        this.uma_compositerole = uma_compositerole;
    }

}