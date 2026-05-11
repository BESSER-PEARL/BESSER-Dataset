





import java.util.List;
import java.util.ArrayList;

public class prosjekt_Course  {

    private String name;
    private int avgGrade;
    private String code;
    private float studyPoints;





    private prosjekt_Institute prosjekt_institute;




    private prosjekt_Institute prosjekt_institute;


    public prosjekt_Course(
        String name,        int avgGrade,        String code,        float studyPoints    ) {
        this.name = name;
        this.avgGrade = avgGrade;
        this.code = code;
        this.studyPoints = studyPoints;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAvggrade() {
        return avgGrade;
    }

    public void setAvggrade(int avgGrade) {
        this.avgGrade = avgGrade;
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

    public prosjekt_Institute getProsjekt_institute() {
        return prosjekt_institute;
    }

    public void setProsjekt_institute(prosjekt_Institute prosjekt_institute) {
        this.prosjekt_institute = prosjekt_institute;
    }
    public prosjekt_Institute getProsjekt_institute() {
        return prosjekt_institute;
    }

    public void setProsjekt_institute(prosjekt_Institute prosjekt_institute) {
        this.prosjekt_institute = prosjekt_institute;
    }

}