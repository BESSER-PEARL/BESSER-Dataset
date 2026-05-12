





import java.util.List;
import java.util.ArrayList;

public class WHISES  {

    private String _id;
    private String statusId;
    private String productId;
    private String userId;
    private String createdAt;





    private PRODUCT product;




    private USER user;


    public WHISES(
        String _id,        String statusId,        String productId,        String userId,        String createdAt    ) {
        this._id = _id;
        this.statusId = statusId;
        this.productId = productId;
        this.userId = userId;
        this.createdAt = createdAt;
    }


    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getStatusid() {
        return statusId;
    }

    public void setStatusid(String statusId) {
        this.statusId = statusId;
    }
    public String getProductid() {
        return productId;
    }

    public void setProductid(String productId) {
        this.productId = productId;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }

    public PRODUCT getProduct() {
        return product;
    }

    public void setProduct(PRODUCT product) {
        this.product = product;
    }
    public USER getUser() {
        return user;
    }

    public void setUser(USER user) {
        this.user = user;
    }

}