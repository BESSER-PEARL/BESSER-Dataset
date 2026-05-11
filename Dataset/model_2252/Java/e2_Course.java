





import java.util.List;
import java.util.ArrayList;

public class e2_Course  {

    private String Name;
    private String ID;
    private float credit;



    public e2_Course(
        String Name,        String ID,        float credit    ) {
        this.Name = Name;
        this.ID = ID;
        this.credit = credit;
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
    public float getCredit() {
        return credit;
    }

    public void setCredit(float credit) {
        this.credit = credit;
    }


}