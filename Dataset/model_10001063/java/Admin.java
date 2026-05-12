





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String id_;
    private String password;



    public Admin(
        String id_,        String password    ) {
        this.id_ = id_;
        this.password = password;
    }


    public String getId_() {
        return id_;
    }

    public void setId_(String id_) {
        this.id_ = id_;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}