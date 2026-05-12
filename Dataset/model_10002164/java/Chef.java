





import java.util.List;
import java.util.ArrayList;

public class Chef  {

    private String name;
    private String staff_Id;



    public Chef(
        String name,        String staff_Id    ) {
        this.name = name;
        this.staff_Id = staff_Id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStaff_id() {
        return staff_Id;
    }

    public void setStaff_id(String staff_Id) {
        this.staff_Id = staff_Id;
    }


}