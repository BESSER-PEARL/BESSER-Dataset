





import java.util.List;
import java.util.ArrayList;

public class programme_Course  {

    private String code;
    private String taugtIn;
    private String level;
    private String name;
    private float credits;





    private programme_Department programme_department;


    public programme_Course(
        String code,        String taugtIn,        String level,        String name,        float credits    ) {
        this.code = code;
        this.taugtIn = taugtIn;
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
    public String getTaugtin() {
        return taugtIn;
    }

    public void setTaugtin(String taugtIn) {
        this.taugtIn = taugtIn;
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
    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
    }

    public programme_Department getProgramme_department() {
        return programme_department;
    }

    public void setProgramme_department(programme_Department programme_department) {
        this.programme_department = programme_department;
    }

}