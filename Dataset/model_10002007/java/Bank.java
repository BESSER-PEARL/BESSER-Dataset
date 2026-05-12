





import java.util.List;
import java.util.ArrayList;

public class Bank  {

    private int code;
    private String address;



    public Bank(
        int code,        String address    ) {
        this.code = code;
        this.address = address;
    }


    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}