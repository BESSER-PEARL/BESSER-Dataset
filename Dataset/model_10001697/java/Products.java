





import java.util.List;
import java.util.ArrayList;

public class Products  {

    private String Name;
    private String Description;
    private int ID;



    public Products(
        String Name,        String Description,        int ID    ) {
        this.Name = Name;
        this.Description = Description;
        this.ID = ID;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }


}