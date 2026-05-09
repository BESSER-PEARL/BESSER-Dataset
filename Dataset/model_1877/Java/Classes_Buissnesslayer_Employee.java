





import java.util.List;
import java.util.ArrayList;

public class Classes_Buissnesslayer_Employee extends User {

    private String Password;
    private int ID;



    public Classes_Buissnesslayer_Employee(
        String Password,        int ID    ) {
        super(
        );
        this.Password = Password;
        this.ID = ID;
    }


    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }


}