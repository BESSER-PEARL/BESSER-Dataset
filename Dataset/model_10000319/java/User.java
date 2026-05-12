





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String email;
    private int Id;
    private String Name;



    public User(
        String email,        int Id,        String Name    ) {
        this.email = email;
        this.Id = Id;
        this.Name = Name;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
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