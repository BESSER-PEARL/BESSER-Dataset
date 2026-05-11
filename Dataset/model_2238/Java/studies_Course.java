





import java.util.List;
import java.util.ArrayList;

public class studies_Course  {

    private String name;
    private float studyPoints;
    private String code;



    public studies_Course(
        String name,        float studyPoints,        String code    ) {
        this.name = name;
        this.studyPoints = studyPoints;
        this.code = code;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getStudypoints() {
        return studyPoints;
    }

    public void setStudypoints(float studyPoints) {
        this.studyPoints = studyPoints;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}