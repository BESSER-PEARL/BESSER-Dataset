





import java.util.List;
import java.util.ArrayList;

public class CATEGORIAS  {

    private String createdAt;
    private String name;
    private String _id;





    private List<PRODUCT> products;


    public CATEGORIAS(
        String createdAt,        String name,        String _id    ) {
        this.createdAt = createdAt;
        this.name = name;
        this._id = _id;
        this.products = new ArrayList<>();
    }

    public CATEGORIAS(
        String createdAt,        String name,        String _id        ArrayList<PRODUCT> products    ) {
        this.createdAt = createdAt;
        this.name = name;
        this._id = _id;
        this.products = products;
    }

    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }

    public List<PRODUCT> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}