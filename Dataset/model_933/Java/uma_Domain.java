





import java.util.List;
import java.util.ArrayList;

public class uma_Domain extends ContentCategory {

    private String workProduct;
    private String group2;





    private List<uma_Domain> uma_domains;


    public uma_Domain(
        String workProduct,        String group2    ) {
        super(
        );
        this.workProduct = workProduct;
        this.group2 = group2;
        this.uma_domains = new ArrayList<>();
    }

    public uma_Domain(
        String workProduct,        String group2        ArrayList<uma_Domain> uma_domains    ) {
        this.workProduct = workProduct;
        this.group2 = group2;
        this.uma_domains = uma_domains;
    }

    public String getWorkproduct() {
        return workProduct;
    }

    public void setWorkproduct(String workProduct) {
        this.workProduct = workProduct;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }

    public List<uma_Domain> getUma_domains() {
        return uma_domains;
    }

    public void addUma_domain(Uma_domain uma_domain) {
        this.uma_domains.add(uma_domain);
    }

}