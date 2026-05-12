





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String ident;
    private String email;
    private String name;
    private int phoneNumber;
    private String surname;



    public Customer(
        String ident,        String email,        String name,        int phoneNumber,        String surname    ) {
        this.ident = ident;
        this.email = email;
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.surname = surname;
    }


    public String getIdent() {
        return ident;
    }

    public void setIdent(String ident) {
        this.ident = ident;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }


}