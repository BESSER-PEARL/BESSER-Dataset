





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String customerName;
    private int phoneNumber;
    private int customerID;





    private List<Address> addresss;


    public Customer(
        String customerName,        int phoneNumber,        int customerID    ) {
        this.customerName = customerName;
        this.phoneNumber = phoneNumber;
        this.customerID = customerID;
        this.addresss = new ArrayList<>();
    }

    public Customer(
        String customerName,        int phoneNumber,        int customerID        ArrayList<Address> addresss    ) {
        this.customerName = customerName;
        this.phoneNumber = phoneNumber;
        this.customerID = customerID;
        this.addresss = addresss;
    }

    public String getCustomername() {
        return customerName;
    }

    public void setCustomername(String customerName) {
        this.customerName = customerName;
    }
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public int getCustomerid() {
        return customerID;
    }

    public void setCustomerid(int customerID) {
        this.customerID = customerID;
    }

    public List<Address> getAddresss() {
        return addresss;
    }

    public void addAddress(Address address) {
        this.addresss.add(address);
    }

}