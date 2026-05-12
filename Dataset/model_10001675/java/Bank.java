





import java.util.List;
import java.util.ArrayList;

public class Bank  {

    private String code;
    private String address;



    public Bank(
        String code,        String address    ) {
        this.code = code;
        this.address = address;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}