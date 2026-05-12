





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String Name;
    private int Receptional_id;



    public Receptionist(
        String Name,        int Receptional_id    ) {
        this.Name = Name;
        this.Receptional_id = Receptional_id;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getReceptional_id() {
        return Receptional_id;
    }

    public void setReceptional_id(int Receptional_id) {
        this.Receptional_id = Receptional_id;
    }


}