





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_ApplianceType_ApplianceService  {

    private float price;
    private String name;



    public ClassDiagram_ApplianceType_ApplianceService(
        float price,        String name    ) {
        this.price = price;
        this.name = name;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}