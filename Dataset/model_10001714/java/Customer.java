





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String lastName;
    private int custId;
    private String firstName;
    private String address;
    private int accountNo;



    public Customer(
        String lastName,        int custId,        String firstName,        String address,        int accountNo    ) {
        this.lastName = lastName;
        this.custId = custId;
        this.firstName = firstName;
        this.address = address;
        this.accountNo = accountNo;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public int getCustid() {
        return custId;
    }

    public void setCustid(int custId) {
        this.custId = custId;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getAccountno() {
        return accountNo;
    }

    public void setAccountno(int accountNo) {
        this.accountNo = accountNo;
    }


}