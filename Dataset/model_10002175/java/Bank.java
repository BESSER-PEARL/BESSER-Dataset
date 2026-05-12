





import java.util.List;
import java.util.ArrayList;

public class Bank  {

    private String address;
    private String code;



    public Bank(
        String address,        String code    ) {
        this.address = address;
        this.code = code;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}