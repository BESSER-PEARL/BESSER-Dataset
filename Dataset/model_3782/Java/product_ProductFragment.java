





import java.util.List;
import java.util.ArrayList;

public class product_ProductFragment extends ProductEntity {

    private String content;





    private product_ProductFragmentContainer product_productfragmentcontainer;


    public product_ProductFragment(
        String content    ) {
        super(
        );
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public product_ProductFragmentContainer getProduct_productfragmentcontainer() {
        return product_productfragmentcontainer;
    }

    public void setProduct_productfragmentcontainer(product_ProductFragmentContainer product_productfragmentcontainer) {
        this.product_productfragmentcontainer = product_productfragmentcontainer;
    }

}