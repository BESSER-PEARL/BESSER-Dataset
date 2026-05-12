





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String name;
    private int Id;



    public Receptionist(
        String name,        int Id    ) {
        this.name = name;
        this.Id = Id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }


}