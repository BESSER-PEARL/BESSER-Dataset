





import java.util.List;
import java.util.ArrayList;

public class zlvp_Anrede  {

    private String name;
    private int id;





    private zlvp_Person zlvp_person;


    public zlvp_Anrede(
        String name,        int id    ) {
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public zlvp_Person getZlvp_person() {
        return zlvp_person;
    }

    public void setZlvp_person(zlvp_Person zlvp_person) {
        this.zlvp_person = zlvp_person;
    }

}