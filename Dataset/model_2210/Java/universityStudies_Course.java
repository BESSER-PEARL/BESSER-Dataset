





import java.util.List;
import java.util.ArrayList;

public class universityStudies_Course  {

    private String credits;
    private String name;
    private int level;
    private String code;



    public universityStudies_Course(
        String credits,        String name,        int level,        String code    ) {
        this.credits = credits;
        this.name = name;
        this.level = level;
        this.code = code;
    }


    public String getCredits() {
        return credits;
    }

    public void setCredits(String credits) {
        this.credits = credits;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}