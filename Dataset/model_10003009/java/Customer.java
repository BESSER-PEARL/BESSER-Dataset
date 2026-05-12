





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String surname;
    private String name;
    private String ident;
    private int phoneNumber;
    private String email;



    public Customer(
        String surname,        String name,        String ident,        int phoneNumber,        String email    ) {
        this.surname = surname;
        this.name = name;
        this.ident = ident;
        this.phoneNumber = phoneNumber;
        this.email = email;
    }


    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
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


}