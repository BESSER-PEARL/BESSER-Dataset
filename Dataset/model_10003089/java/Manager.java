





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private String Name;
    private int Id;
    private int Phone_No;



    public Manager(
        String Name,        int Id,        int Phone_No    ) {
        this.Name = Name;
        this.Id = Id;
        this.Phone_No = Phone_No;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public int getPhone_no() {
        return Phone_No;
    }

    public void setPhone_no(int Phone_No) {
        this.Phone_No = Phone_No;
    }


}