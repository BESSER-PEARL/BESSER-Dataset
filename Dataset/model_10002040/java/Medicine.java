





import java.util.List;
import java.util.ArrayList;

public class Medicine  {

    private String price;
    private String type;
    private String name;
    private int code;



    public Medicine(
        String price,        String type,        String name,        int code    ) {
        this.price = price;
        this.type = type;
        this.name = name;
        this.code = code;
    }


    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
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
    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }


}