





import java.util.List;
import java.util.ArrayList;

public class studyprogram_Course  {

    private String name;
    private String semester;
    private String code;
    private String credits;



    public studyprogram_Course(
        String name,        String semester,        String code,        String credits    ) {
        this.name = name;
        this.semester = semester;
        this.code = code;
        this.credits = credits;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSemester() {
        return semester;
    }

    public void setSemester(String semester) {
        this.semester = semester;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getCredits() {
        return credits;
    }

    public void setCredits(String credits) {
        this.credits = credits;
    }


}