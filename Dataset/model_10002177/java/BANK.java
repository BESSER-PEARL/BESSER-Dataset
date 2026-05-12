





import java.util.List;
import java.util.ArrayList;

public class BANK  {

    private String Code;
    private String Address;



    public BANK(
        String Code,        String Address    ) {
        this.Code = Code;
        this.Address = Address;
    }


    public String getCode() {
        return Code;
    }

    public void setCode(String Code) {
        this.Code = Code;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }


}