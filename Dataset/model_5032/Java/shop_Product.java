





import java.util.List;
import java.util.ArrayList;

public class shop_Product  {

    private String number;
    private String name;
    private String description;



    public shop_Product(
        String number,        String name,        String description    ) {
        this.number = number;
        this.name = name;
        this.description = description;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}