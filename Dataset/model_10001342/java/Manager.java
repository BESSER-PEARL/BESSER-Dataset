





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private int Phone_No;
    private int Id;
    private String Name;



    public Manager(
        int Phone_No,        int Id,        String Name    ) {
        this.Phone_No = Phone_No;
        this.Id = Id;
        this.Name = Name;
    }


    public int getPhone_no() {
        return Phone_No;
    }

    public void setPhone_no(int Phone_No) {
        this.Phone_No = Phone_No;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}