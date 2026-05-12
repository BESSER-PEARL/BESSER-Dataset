





import java.util.List;
import java.util.ArrayList;

public class Cash_on_delievery  {

    private int Phone_number;
    private String Customer_Name;
    private String Address;
    private String Amount;



    public Cash_on_delievery(
        int Phone_number,        String Customer_Name,        String Address,        String Amount    ) {
        this.Phone_number = Phone_number;
        this.Customer_Name = Customer_Name;
        this.Address = Address;
        this.Amount = Amount;
    }


    public int getPhone_number() {
        return Phone_number;
    }

    public void setPhone_number(int Phone_number) {
        this.Phone_number = Phone_number;
    }
    public String getCustomer_name() {
        return Customer_Name;
    }

    public void setCustomer_name(String Customer_Name) {
        this.Customer_Name = Customer_Name;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getAmount() {
        return Amount;
    }

    public void setAmount(String Amount) {
        this.Amount = Amount;
    }


}