





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String CutsomerAddress;
    private String Email;
    private String CustomerName;
    private int PhoneNumber;



    public Customer(
        String CutsomerAddress,        String Email,        String CustomerName,        int PhoneNumber    ) {
        this.CutsomerAddress = CutsomerAddress;
        this.Email = Email;
        this.CustomerName = CustomerName;
        this.PhoneNumber = PhoneNumber;
    }


    public String getCutsomeraddress() {
        return CutsomerAddress;
    }

    public void setCutsomeraddress(String CutsomerAddress) {
        this.CutsomerAddress = CutsomerAddress;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getCustomername() {
        return CustomerName;
    }

    public void setCustomername(String CustomerName) {
        this.CustomerName = CustomerName;
    }
    public int getPhonenumber() {
        return PhoneNumber;
    }

    public void setPhonenumber(int PhoneNumber) {
        this.PhoneNumber = PhoneNumber;
    }


}