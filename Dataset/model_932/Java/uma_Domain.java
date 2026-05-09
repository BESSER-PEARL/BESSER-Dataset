





import java.util.List;
import java.util.ArrayList;

public class uma_Domain extends ContentCategory {






    private uma_Domain uma_domain;




    private List<uma_WorkProduct> uma_workproducts;


    public uma_Domain(
    ) {
        super(
        );
        this.uma_workproducts = new ArrayList<>();
    }

    public uma_Domain(
        ArrayList<uma_WorkProduct> uma_workproducts    ) {
        this.uma_workproducts = uma_workproducts;
    }


    public uma_Domain getUma_domain() {
        return uma_domain;
    }

    public void setUma_domain(uma_Domain uma_domain) {
        this.uma_domain = uma_domain;
    }
    public List<uma_WorkProduct> getUma_workproducts() {
        return uma_workproducts;
    }

    public void addUma_workproduct(Uma_workproduct uma_workproduct) {
        this.uma_workproducts.add(uma_workproduct);
    }

}