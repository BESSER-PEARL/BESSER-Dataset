





import java.util.List;
import java.util.ArrayList;

public class Subject  {

    private int id;
    private String subjectName;
    private int subjectCode;



    public Subject(
        int id,        String subjectName,        int subjectCode    ) {
        this.id = id;
        this.subjectName = subjectName;
        this.subjectCode = subjectCode;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getSubjectname() {
        return subjectName;
    }

    public void setSubjectname(String subjectName) {
        this.subjectName = subjectName;
    }
    public int getSubjectcode() {
        return subjectCode;
    }

    public void setSubjectcode(int subjectCode) {
        this.subjectCode = subjectCode;
    }


}