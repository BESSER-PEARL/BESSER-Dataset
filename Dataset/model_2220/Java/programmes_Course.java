





import java.util.List;
import java.util.ArrayList;

public class programmes_Course  {

    private float credits;
    private String level;
    private String code;
    private String name;



    public programmes_Course(
        float credits,        String level,        String code,        String name    ) {
        this.credits = credits;
        this.level = level;
        this.code = code;
        this.name = name;
    }


    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
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


}