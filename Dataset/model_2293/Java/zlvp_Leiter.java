





import java.util.List;
import java.util.ArrayList;

public class zlvp_Leiter  {

    private int id;





    private zlvp_Person zlvp_person;


    public zlvp_Leiter(
        int id    ) {
        this.id = id;
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