





import java.util.List;
import java.util.ArrayList;

public class MediDevices  {

    private String type;
    private String name;
    private String id;





    private Product product;


    public MediDevices(
        String type,        String name,        String id    ) {
        this.type = type;
        this.name = name;
        this.id = id;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}