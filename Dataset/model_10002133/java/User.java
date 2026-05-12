





import java.util.List;
import java.util.ArrayList;

public class User  {

    private int UserHash;
    private String UserName;
    private String UserNameFull;
    private String EmailAddress;
    private String FirstName;
    private String Password;
    private String LastName;
    private int Id;



    public User(
        int UserHash,        String UserName,        String UserNameFull,        String EmailAddress,        String FirstName,        String Password,        String LastName,        int Id    ) {
        this.UserHash = UserHash;
        this.UserName = UserName;
        this.UserNameFull = UserNameFull;
        this.EmailAddress = EmailAddress;
        this.FirstName = FirstName;
        this.Password = Password;
        this.LastName = LastName;
        this.Id = Id;
    }


    public int getUserhash() {
        return UserHash;
    }

    public void setUserhash(int UserHash) {
        this.UserHash = UserHash;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getUsernamefull() {
        return UserNameFull;
    }

    public void setUsernamefull(String UserNameFull) {
        this.UserNameFull = UserNameFull;
    }
    public String getEmailaddress() {
        return EmailAddress;
    }

    public void setEmailaddress(String EmailAddress) {
        this.EmailAddress = EmailAddress;
    }
    public String getFirstname() {
        return FirstName;
    }

    public void setFirstname(String FirstName) {
        this.FirstName = FirstName;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getLastname() {
        return LastName;
    }

    public void setLastname(String LastName) {
        this.LastName = LastName;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }


}