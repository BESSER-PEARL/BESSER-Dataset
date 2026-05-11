





import java.util.List;
import java.util.ArrayList;

public class study_Course  {

    private float points;
    private String code;
    private String name;





    private study_Department study_department;


    public study_Course(
        float points,        String code,        String name    ) {
        this.points = points;
        this.code = code;
        this.name = name;
    }


    public float getPoints() {
        return points;
    }

    public void setPoints(float points) {
        this.points = points;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public study_Department getStudy_department() {
        return study_department;
    }

    public void setStudy_department(study_Department study_department) {
        this.study_department = study_department;
    }

}