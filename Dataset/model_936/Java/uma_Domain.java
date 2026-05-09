





import java.util.List;
import java.util.ArrayList;

public class uma_Domain extends ContentCategory {

    private String group2;
    private String workProduct;





    private uma_Domain uma_domain;


    public uma_Domain(
        String group2,        String workProduct    ) {
        super(
        );
        this.group2 = group2;
        this.workProduct = workProduct;
    }


    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getWorkproduct() {
        return workProduct;
    }

    public void setWorkproduct(String workProduct) {
        this.workProduct = workProduct;
    }

    public uma_Domain getUma_domain() {
        return uma_domain;
    }

    public void setUma_domain(uma_Domain uma_domain) {
        this.uma_domain = uma_domain;
    }

}