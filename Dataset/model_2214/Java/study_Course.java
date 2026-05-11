





import java.util.List;
import java.util.ArrayList;

public class study_Course  {

    private int level;
    private float credits;
    private String code;
    private String name;



    public study_Course(
        int level,        float credits,        String code,        String name    ) {
        this.level = level;
        this.credits = credits;
        this.code = code;
        this.name = name;
    }


    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
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


}