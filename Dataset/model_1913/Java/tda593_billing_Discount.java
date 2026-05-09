





import java.util.List;
import java.util.ArrayList;

public class tda593_billing_Discount  {

    private String code;
    private String name;



    public tda593_billing_Discount(
        String code,        String name    ) {
        this.code = code;
        this.name = name;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}