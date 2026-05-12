





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String surname;
    private String ident;
    private String name;
    private int phoneNumber;
    private String email;



    public Customer(
        String surname,        String ident,        String name,        int phoneNumber,        String email    ) {
        this.surname = surname;
        this.ident = ident;
        this.name = name;
        this.phoneNumber = phoneNumber;
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