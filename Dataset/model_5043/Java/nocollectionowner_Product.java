





import java.util.List;
import java.util.ArrayList;

public class nocollectionowner_Product  {

    private String number;
    private String description;
    private String name;



    public nocollectionowner_Product(
        String number,        String description,        String name    ) {
        this.number = number;
        this.description = description;
        this.name = name;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}