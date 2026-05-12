





import java.util.List;
import java.util.ArrayList;

public class Submit_information  {

    private String password_;
    private String name_;
    private String username;
    private String phone_;





    private Userguest userguest;


    public Submit_information(
        String password_,        String name_,        String username,        String phone_    ) {
        this.password_ = password_;
        this.name_ = name_;
        this.username = username;
        this.phone_ = phone_;
    }


    public String getPassword_() {
        return password_;
    }

    public void setPassword_(String password_) {
        this.password_ = password_;
    }
    public String getName_() {
        return name_;
    }

    public void setName_(String name_) {
        this.name_ = name_;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPhone_() {
        return phone_;
    }

    public void setPhone_(String phone_) {
        this.phone_ = phone_;
    }

    public Userguest getUserguest() {
        return userguest;
    }

    public void setUserguest(Userguest userguest) {
        this.userguest = userguest;
    }

}