





import java.util.List;
import java.util.ArrayList;

public class BANK  {

    private String Code;
    private String Address;
    private String attribute;



    public BANK(
        String Code,        String Address,        String attribute    ) {
        this.Code = Code;
        this.Address = Address;
        this.attribute = attribute;
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
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}