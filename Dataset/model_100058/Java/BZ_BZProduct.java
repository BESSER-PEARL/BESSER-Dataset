





import java.util.List;
import java.util.ArrayList;

public class BZ_BZProduct  {

    private String productDescription;
    private String productId;
    private String productURL;





    private BZ_BZRepo bz_bzrepo;




    private BZ_BZRepo bz_bzrepo;


    public BZ_BZProduct(
        String productDescription,        String productId,        String productURL    ) {
        this.productDescription = productDescription;
        this.productId = productId;
        this.productURL = productURL;
    }


    public String getProductdescription() {
        return productDescription;
    }

    public void setProductdescription(String productDescription) {
        this.productDescription = productDescription;
    }
    public String getProductid() {
        return productId;
    }

    public void setProductid(String productId) {
        this.productId = productId;
    }
    public String getProducturl() {
        return productURL;
    }

    public void setProducturl(String productURL) {
        this.productURL = productURL;
    }

    public BZ_BZRepo getBz_bzrepo() {
        return bz_bzrepo;
    }

    public void setBz_bzrepo(BZ_BZRepo bz_bzrepo) {
        this.bz_bzrepo = bz_bzrepo;
    }
    public BZ_BZRepo getBz_bzrepo() {
        return bz_bzrepo;
    }

    public void setBz_bzrepo(BZ_BZRepo bz_bzrepo) {
        this.bz_bzrepo = bz_bzrepo;
    }

}