





import java.util.List;
import java.util.ArrayList;

public class Submit_information  {

    private String phone_;
    private String username;
    private String name_;
    private String password_;





    private Userguest userguest;


    public Submit_information(
        String phone_,        String username,        String name_,        String password_    ) {
        this.phone_ = phone_;
        this.username = username;
        this.name_ = name_;
        this.password_ = password_;
    }


    public String getPhone_() {
        return phone_;
    }

    public void setPhone_(String phone_) {
        this.phone_ = phone_;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getName_() {
        return name_;
    }

    public void setName_(String name_) {
        this.name_ = name_;
    }
    public String getPassword_() {
        return password_;
    }

    public void setPassword_(String password_) {
        this.password_ = password_;
    }

    public Userguest getUserguest() {
        return userguest;
    }

    public void setUserguest(Userguest userguest) {
        this.userguest = userguest;
    }

}