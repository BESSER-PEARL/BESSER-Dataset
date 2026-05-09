





import java.util.List;
import java.util.ArrayList;

public class uma_Role extends ContentElement, FulfillableElement {






    private List<uma_WorkProduct> uma_workproducts;




    private List<uma_WorkProduct> uma_workproducts;


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

}