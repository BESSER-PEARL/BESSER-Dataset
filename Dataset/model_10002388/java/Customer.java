





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String surname;
    private int phoneNumber;
    private String name;
    private String ident;
    private String email;



    public Customer(
        String surname,        int phoneNumber,        String name,        String ident,        String email    ) {
        this.surname = surname;
        this.phoneNumber = phoneNumber;
        this.name = name;
        this.ident = ident;
        this.email = email;
    }


    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
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


}