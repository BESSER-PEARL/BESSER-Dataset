





import java.util.List;
import java.util.ArrayList;

public class customers_Address  {

    private String town;
    private String street;
    private String zipCode;





    private customers_Customer customers_customer;


    public customers_Address(
        String town,        String street,        String zipCode    ) {
        this.town = town;
        this.street = street;
        this.zipCode = zipCode;
    }


    public String getTown() {
        return town;
    }

    public void setTown(String town) {
        this.town = town;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
    }

    public customers_Customer getCustomers_customer() {
        return customers_customer;
    }

    public void setCustomers_customer(customers_Customer customers_customer) {
        this.customers_customer = customers_customer;
    }

}