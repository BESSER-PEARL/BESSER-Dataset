





import java.util.List;
import java.util.ArrayList;

public class uma_WorkProductType extends ContentCategory {

    private String workProduct;
    private String group2;



    public uma_WorkProductType(
        String workProduct,        String group2    ) {
        super(
        );
        this.workProduct = workProduct;
        this.group2 = group2;
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


}