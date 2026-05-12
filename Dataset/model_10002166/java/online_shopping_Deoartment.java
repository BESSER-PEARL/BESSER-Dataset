





import java.util.List;
import java.util.ArrayList;

public class online_shopping_Deoartment  {

    private String Department_ID;
    private String Name;
    private String Description;



    public online_shopping_Deoartment(
        String Department_ID,        String Name,        String Description    ) {
        this.Department_ID = Department_ID;
        this.Name = Name;
        this.Description = Description;
    }


    public String getDepartment_id() {
        return Department_ID;
    }

    public void setDepartment_id(String Department_ID) {
        this.Department_ID = Department_ID;
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


}