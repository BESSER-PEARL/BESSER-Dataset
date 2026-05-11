





import java.util.List;
import java.util.ArrayList;

public class prosjekt_Course  {

    private String name;
    private String code;
    private float studyPoints;





    private prosjekt_Department prosjekt_department;




    private prosjekt_Department prosjekt_department;


    public prosjekt_Course(
        String name,        String code,        float studyPoints    ) {
        this.name = name;
        this.code = code;
        this.studyPoints = studyPoints;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public float getStudypoints() {
        return studyPoints;
    }

    public void setStudypoints(float studyPoints) {
        this.studyPoints = studyPoints;
    }

    public prosjekt_Department getProsjekt_department() {
        return prosjekt_department;
    }

    public void setProsjekt_department(prosjekt_Department prosjekt_department) {
        this.prosjekt_department = prosjekt_department;
    }
    public prosjekt_Department getProsjekt_department() {
        return prosjekt_department;
    }

    public void setProsjekt_department(prosjekt_Department prosjekt_department) {
        this.prosjekt_department = prosjekt_department;
    }

}