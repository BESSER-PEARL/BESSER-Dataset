





import java.util.List;
import java.util.ArrayList;

public class StudyField  {

    private String name;
    private None subjects;
    private int id;
    private int subjectsCount;
    private int currentId;



    public StudyField(
        String name,        None subjects,        int id,        int subjectsCount,        int currentId    ) {
        this.name = name;
        this.subjects = subjects;
        this.id = id;
        this.subjectsCount = subjectsCount;
        this.currentId = currentId;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getSubjects() {
        return subjects;
    }

    public void setSubjects(None subjects) {
        this.subjects = subjects;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getSubjectscount() {
        return subjectsCount;
    }

    public void setSubjectscount(int subjectsCount) {
        this.subjectsCount = subjectsCount;
    }
    public int getCurrentid() {
        return currentId;
    }

    public void setCurrentid(int currentId) {
        this.currentId = currentId;
    }


}