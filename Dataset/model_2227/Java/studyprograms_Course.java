





import java.util.List;
import java.util.ArrayList;

public class studyprograms_Course  {

    private String level;
    private String code;
    private String name;
    private float ects;
    private String availableSemester;



    public studyprograms_Course(
        String level,        String code,        String name,        float ects,        String availableSemester    ) {
        this.level = level;
        this.code = code;
        this.name = name;
        this.ects = ects;
        this.availableSemester = availableSemester;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
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
    public float getEcts() {
        return ects;
    }

    public void setEcts(float ects) {
        this.ects = ects;
    }
    public String getAvailablesemester() {
        return availableSemester;
    }

    public void setAvailablesemester(String availableSemester) {
        this.availableSemester = availableSemester;
    }


}