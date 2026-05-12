





import java.util.List;
import java.util.ArrayList;

public class Cash_on_delievery  {

    private String Amount;
    private String Address;
    private String Customer_Name;
    private int Phone_number;



    public Cash_on_delievery(
        String Amount,        String Address,        String Customer_Name,        int Phone_number    ) {
        this.Amount = Amount;
        this.Address = Address;
        this.Customer_Name = Customer_Name;
        this.Phone_number = Phone_number;
    }


    public String getAmount() {
        return Amount;
    }

    public void setAmount(String Amount) {
        this.Amount = Amount;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getCustomer_name() {
        return Customer_Name;
    }

    public void setCustomer_name(String Customer_Name) {
        this.Customer_Name = Customer_Name;
    }
    public int getPhone_number() {
        return Phone_number;
    }

    public void setPhone_number(int Phone_number) {
        this.Phone_number = Phone_number;
    }


}