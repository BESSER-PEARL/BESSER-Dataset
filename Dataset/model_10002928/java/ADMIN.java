





import java.util.List;
import java.util.ArrayList;

public class ADMIN  {

    private String Code;
    private String Address;



    public ADMIN(
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