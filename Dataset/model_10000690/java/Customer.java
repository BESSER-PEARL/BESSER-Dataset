





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int phoneNumber;
    private String email;
    private String surname;
    private String ident;
    private String name;



    public Customer(
        int phoneNumber,        String email,        String surname,        String ident,        String name    ) {
        this.phoneNumber = phoneNumber;
        this.email = email;
        this.surname = surname;
        this.ident = ident;
        this.name = name;
    }


    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }
    public String getIdent() {
        return ident;
    }

    public void setIdent(String ident) {
        this.ident = ident;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}