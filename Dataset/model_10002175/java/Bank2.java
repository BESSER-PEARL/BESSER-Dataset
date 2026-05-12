





import java.util.List;
import java.util.ArrayList;

public class Bank2  {

    private String code;
    private String address;



    public Bank2(
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