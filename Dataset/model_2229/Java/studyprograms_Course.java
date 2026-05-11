





import java.util.List;
import java.util.ArrayList;

public class studyprograms_Course  {

    private float ects;
    private String level;
    private String name;
    private String code;
    private String availableSemester;



    public studyprograms_Course(
        float ects,        String level,        String name,        String code,        String availableSemester    ) {
        this.ects = ects;
        this.level = level;
        this.name = name;
        this.code = code;
        this.availableSemester = availableSemester;
    }


    public float getEcts() {
        return ects;
    }

    public void setEcts(float ects) {
        this.ects = ects;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
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
    public String getAvailablesemester() {
        return availableSemester;
    }

    public void setAvailablesemester(String availableSemester) {
        this.availableSemester = availableSemester;
    }


}