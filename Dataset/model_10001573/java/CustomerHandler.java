





import java.util.List;
import java.util.ArrayList;

public class CustomerHandler  {

    private String populate;
    private None state;
    private String password;



    public CustomerHandler(
        String populate,        None state,        String password    ) {
        this.populate = populate;
        this.state = state;
        this.password = password;
    }


    public String getPopulate() {
        return populate;
    }

    public void setPopulate(String populate) {
        this.populate = populate;
    }
    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}