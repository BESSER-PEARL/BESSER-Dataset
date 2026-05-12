





import java.util.List;
import java.util.ArrayList;

public class UserRoles  {

    private String Name;
    private int Id;



    public UserRoles(
        String Name,        int Id    ) {
        this.Name = Name;
        this.Id = Id;
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


}