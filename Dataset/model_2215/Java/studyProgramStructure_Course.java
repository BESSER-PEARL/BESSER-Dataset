





import java.util.List;
import java.util.ArrayList;

public class studyProgramStructure_Course  {

    private String code;
    private int level;
    private String name;
    private float credits;



    public studyProgramStructure_Course(
        String code,        int level,        String name,        float credits    ) {
        this.code = code;
        this.level = level;
        this.name = name;
        this.credits = credits;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
    }


}