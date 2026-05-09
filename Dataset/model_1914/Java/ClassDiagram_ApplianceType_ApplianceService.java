





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_ApplianceType_ApplianceService  {

    private String name;
    private float price;



    public ClassDiagram_ApplianceType_ApplianceService(
        String name,        float price    ) {
        this.name = name;
        this.price = price;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }


}