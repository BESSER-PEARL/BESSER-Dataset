





import java.util.List;
import java.util.ArrayList;

public class uma_Role extends FulfillableElement, ContentElement {






    private uma_Task uma_task;




    private List<uma_WorkProduct> uma_workproducts;




    private List<uma_WorkProduct> uma_workproducts;




    private uma_Task uma_task;


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


    public uma_Task getUma_task() {
        return uma_task;
    }

    public void setUma_task(uma_Task uma_task) {
        this.uma_task = uma_task;
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
    public uma_Task getUma_task() {
        return uma_task;
    }

    public void setUma_task(uma_Task uma_task) {
        this.uma_task = uma_task;
    }

}