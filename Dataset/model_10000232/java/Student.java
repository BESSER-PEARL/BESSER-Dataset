





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String ID;
    private String Name;



    public Student(
        String ID,        String Name    ) {
        this.ID = ID;
        this.Name = Name;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}