





import java.util.List;
import java.util.ArrayList;

public class Exam  {

    private String id;
    private None subject;
    private int points;
    private String name;
    private int currentId;



    public Exam(
        String id,        None subject,        int points,        String name,        int currentId    ) {
        this.id = id;
        this.subject = subject;
        this.points = points;
        this.name = name;
        this.currentId = currentId;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public None getSubject() {
        return subject;
    }

    public void setSubject(None subject) {
        this.subject = subject;
    }
    public int getPoints() {
        return points;
    }

    public void setPoints(int points) {
        this.points = points;
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