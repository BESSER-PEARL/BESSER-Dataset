





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String DOB;
    private int Phone;
    private String LastName;
    private String Name;
    private String Email;
    private String Address;





    private Product product;




    private Registration registration;


    public Person(
        String DOB,        int Phone,        String LastName,        String Name,        String Email,        String Address    ) {
        this.DOB = DOB;
        this.Phone = Phone;
        this.LastName = LastName;
        this.Name = Name;
        this.Email = Email;
        this.Address = Address;
    }


    public String getDob() {
        return DOB;
    }

    public void setDob(String DOB) {
        this.DOB = DOB;
    }
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }
    public String getLastname() {
        return LastName;
    }

    public void setLastname(String LastName) {
        this.LastName = LastName;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }
    public Registration getRegistration() {
        return registration;
    }

    public void setRegistration(Registration registration) {
        this.registration = registration;
    }

}