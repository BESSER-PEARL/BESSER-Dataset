





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String id;
    private String name;
    private String supplier;



    public Product(
        String id,        String name,        String supplier    ) {
        this.id = id;
        this.name = name;
        this.supplier = supplier;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSupplier() {
        return supplier;
    }

    public void setSupplier(String supplier) {
        this.supplier = supplier;
    }


}