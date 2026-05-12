





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String Name;
    private String ID;



    public Student(
        String Name,        String ID    ) {
        this.Name = Name;
        this.ID = ID;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }


}