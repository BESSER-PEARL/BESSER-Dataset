





import java.util.List;
import java.util.ArrayList;

public class Manager1  {

    private String Password;
    private String Name;
    private int Manager_id;



    public Manager1(
        String Password,        String Name,        int Manager_id    ) {
        this.Password = Password;
        this.Name = Name;
        this.Manager_id = Manager_id;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getManager_id() {
        return Manager_id;
    }

    public void setManager_id(int Manager_id) {
        this.Manager_id = Manager_id;
    }


}