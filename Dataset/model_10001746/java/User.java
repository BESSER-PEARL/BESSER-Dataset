





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Surname;
    private int Age;
    private String Name;
    private String HomeAddress;
    private String Email;



    public User(
        String Surname,        int Age,        String Name,        String HomeAddress,        String Email    ) {
        this.Surname = Surname;
        this.Age = Age;
        this.Name = Name;
        this.HomeAddress = HomeAddress;
        this.Email = Email;
    }


    public String getSurname() {
        return Surname;
    }

    public void setSurname(String Surname) {
        this.Surname = Surname;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getHomeaddress() {
        return HomeAddress;
    }

    public void setHomeaddress(String HomeAddress) {
        this.HomeAddress = HomeAddress;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }


}