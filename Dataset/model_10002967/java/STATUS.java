





import java.util.List;
import java.util.ArrayList;

public class STATUS  {

    private String createdAt;
    private String _id;
    private String name;





    private PRODUCT product;


    public STATUS(
        String createdAt,        String _id,        String name    ) {
        this.createdAt = createdAt;
        this._id = _id;
        this.name = name;
    }


    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PRODUCT getProduct() {
        return product;
    }

    public void setProduct(PRODUCT product) {
        this.product = product;
    }

}