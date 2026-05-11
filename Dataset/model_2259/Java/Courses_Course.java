





import java.util.List;
import java.util.ArrayList;

public class Courses_Course  {

    private String name;
    private String id;
    private float credit;



    public Courses_Course(
        String name,        String id,        float credit    ) {
        this.name = name;
        this.id = id;
        this.credit = credit;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public float getCredit() {
        return credit;
    }

    public void setCredit(float credit) {
        this.credit = credit;
    }


}