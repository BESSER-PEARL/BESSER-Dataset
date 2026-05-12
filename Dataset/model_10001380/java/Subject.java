





import java.util.List;
import java.util.ArrayList;

public class Subject  {

    private int credits;
    private int id;
    private String name;
    private int currentId;



    public Subject(
        int credits,        int id,        String name,        int currentId    ) {
        this.credits = credits;
        this.id = id;
        this.name = name;
        this.currentId = currentId;
    }


    public int getCredits() {
        return credits;
    }

    public void setCredits(int credits) {
        this.credits = credits;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCurrentid() {
        return currentId;
    }

    public void setCurrentid(int currentId) {
        this.currentId = currentId;
    }


}