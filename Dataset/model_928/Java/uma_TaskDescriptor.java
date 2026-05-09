





import java.util.List;
import java.util.ArrayList;

public class uma_TaskDescriptor extends WorkBreakdownElement, Descriptor {






    private List<uma_WorkProduct> uma_workproducts;




    private List<uma_Section> uma_sections;




    private List<uma_WorkProduct> uma_workproducts;




    private List<uma_Role> uma_roles;




    private List<uma_WorkProduct> uma_workproducts;




    private List<uma_Section> uma_sections;




    private List<uma_Role> uma_roles;




    private uma_Task uma_task;


    public uma_TaskDescriptor(
    ) {
        super(
        );
        this.uma_workproducts = new ArrayList<>();
        this.uma_sections = new ArrayList<>();
        this.uma_workproducts = new ArrayList<>();
        this.uma_roles = new ArrayList<>();
        this.uma_workproducts = new ArrayList<>();
        this.uma_sections = new ArrayList<>();
        this.uma_roles = new ArrayList<>();
    }

    public uma_TaskDescriptor(
        ArrayList<uma_WorkProduct> uma_workproducts,        ArrayList<uma_Section> uma_sections,        ArrayList<uma_WorkProduct> uma_workproducts,        ArrayList<uma_Role> uma_roles,        ArrayList<uma_WorkProduct> uma_workproducts,        ArrayList<uma_Section> uma_sections,        ArrayList<uma_Role> uma_roles    ) {
        this.uma_workproducts = uma_workproducts;
        this.uma_sections = uma_sections;
        this.uma_workproducts = uma_workproducts;
        this.uma_roles = uma_roles;
        this.uma_workproducts = uma_workproducts;
        this.uma_sections = uma_sections;
        this.uma_roles = uma_roles;
    }


    public List<uma_WorkProduct> getUma_workproducts() {
        return uma_workproducts;
    }

    public void addUma_workproduct(Uma_workproduct uma_workproduct) {
        this.uma_workproducts.add(uma_workproduct);
    }
    public List<uma_Section> getUma_sections() {
        return uma_sections;
    }

    public void addUma_section(Uma_section uma_section) {
        this.uma_sections.add(uma_section);
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
    public List<uma_Section> getUma_sections() {
        return uma_sections;
    }

    public void addUma_section(Uma_section uma_section) {
        this.uma_sections.add(uma_section);
    }
    public List<uma_Role> getUma_roles() {
        return uma_roles;
    }

    public void addUma_role(Uma_role uma_role) {
        this.uma_roles.add(uma_role);
    }
    public uma_Task getUma_task() {
        return uma_task;
    }

    public void setUma_task(uma_Task uma_task) {
        this.uma_task = uma_task;
    }

}