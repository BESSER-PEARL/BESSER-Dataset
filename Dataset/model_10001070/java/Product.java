





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String name;
    private String id;
    private String supplier;



    public Product(
        String name,        String id,        String supplier    ) {
        this.name = name;
        this.id = id;
        this.supplier = supplier;
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
    public String getSupplier() {
        return supplier;
    }

    public void setSupplier(String supplier) {
        this.supplier = supplier;
    }


}