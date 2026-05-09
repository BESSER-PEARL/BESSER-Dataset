





import java.util.List;
import java.util.ArrayList;

public class uma_Domain extends ContentCategory {






    private List<uma_Domain> uma_domains;




    private List<uma_WorkProduct> uma_workproducts;


    public uma_Domain(
    ) {
        super(
        );
        this.uma_domains = new ArrayList<>();
        this.uma_workproducts = new ArrayList<>();
    }

    public uma_Domain(
        ArrayList<uma_Domain> uma_domains,        ArrayList<uma_WorkProduct> uma_workproducts    ) {
        this.uma_domains = uma_domains;
        this.uma_workproducts = uma_workproducts;
    }


    public List<uma_Domain> getUma_domains() {
        return uma_domains;
    }

    public void addUma_domain(Uma_domain uma_domain) {
        this.uma_domains.add(uma_domain);
    }
    public List<uma_WorkProduct> getUma_workproducts() {
        return uma_workproducts;
    }

    public void addUma_workproduct(Uma_workproduct uma_workproduct) {
        this.uma_workproducts.add(uma_workproduct);
    }

}