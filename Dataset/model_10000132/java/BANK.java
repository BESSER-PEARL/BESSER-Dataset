





import java.util.List;
import java.util.ArrayList;

public class BANK  {

    private String Address;
    private String Code;



    public BANK(
        String Address,        String Code    ) {
        this.Address = Address;
        this.Code = Code;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getCode() {
        return Code;
    }

    public void setCode(String Code) {
        this.Code = Code;
    }


}