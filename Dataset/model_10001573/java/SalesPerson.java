





import java.util.List;
import java.util.ArrayList;

public class SalesPerson  {

    private String password;
    private String populate;
    private None state;



    public SalesPerson(
        String password,        String populate,        None state    ) {
        this.password = password;
        this.populate = populate;
        this.state = state;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
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


}