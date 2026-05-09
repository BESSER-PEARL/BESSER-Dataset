





import java.util.List;
import java.util.ArrayList;

public class uma_RoleDescriptor extends Descriptor {






    private uma_TaskDescriptor uma_taskdescriptor;




    private List<uma_WorkProductDescriptor> uma_workproductdescriptors;




    private uma_TaskDescriptor uma_taskdescriptor;




    private List<uma_WorkProductDescriptor> uma_workproductdescriptors;




    private uma_TaskDescriptor uma_taskdescriptor;




    private uma_TeamProfile uma_teamprofile;




    private List<uma_WorkProduct> uma_workproducts;




    private uma_Role uma_role;


    public uma_RoleDescriptor(
    ) {
        super(
        );
        this.uma_workproductdescriptors = new ArrayList<>();
        this.uma_workproductdescriptors = new ArrayList<>();
        this.uma_workproducts = new ArrayList<>();
    }

    public uma_RoleDescriptor(
        ArrayList<uma_WorkProductDescriptor> uma_workproductdescriptors,        ArrayList<uma_WorkProductDescriptor> uma_workproductdescriptors,        ArrayList<uma_WorkProduct> uma_workproducts    ) {
        this.uma_workproductdescriptors = uma_workproductdescriptors;
        this.uma_workproductdescriptors = uma_workproductdescriptors;
        this.uma_workproducts = uma_workproducts;
    }


    public uma_TaskDescriptor getUma_taskdescriptor() {
        return uma_taskdescriptor;
    }

    public void setUma_taskdescriptor(uma_TaskDescriptor uma_taskdescriptor) {
        this.uma_taskdescriptor = uma_taskdescriptor;
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
    public uma_TeamProfile getUma_teamprofile() {
        return uma_teamprofile;
    }

    public void setUma_teamprofile(uma_TeamProfile uma_teamprofile) {
        this.uma_teamprofile = uma_teamprofile;
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

}