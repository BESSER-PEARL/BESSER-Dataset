





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String surname;
    private String ident;
    private String email;
    private int phoneNumber;
    private String name;



    public Customer(
        String surname,        String ident,        String email,        int phoneNumber,        String name    ) {
        this.surname = surname;
        this.ident = ident;
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.name = name;
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
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}