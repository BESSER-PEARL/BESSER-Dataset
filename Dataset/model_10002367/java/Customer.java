





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String surname;
    private String email;
    private String name;
    private String ident;
    private int phoneNumber;



    public Customer(
        String surname,        String email,        String name,        String ident,        int phoneNumber    ) {
        this.surname = surname;
        this.email = email;
        this.name = name;
        this.ident = ident;
        this.phoneNumber = phoneNumber;
    }


    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
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


}