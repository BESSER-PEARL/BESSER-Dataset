





import java.util.List;
import java.util.ArrayList;

public class CodePack_DataModels_ServiceType  {

    private float price;
    private String type_name;
    private String description;



    public CodePack_DataModels_ServiceType(
        float price,        String type_name,        String description    ) {
        this.price = price;
        this.type_name = type_name;
        this.description = description;
    }


    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getType_name() {
        return type_name;
    }

    public void setType_name(String type_name) {
        this.type_name = type_name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}