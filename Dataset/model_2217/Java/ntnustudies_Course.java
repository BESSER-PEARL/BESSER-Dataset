





import java.util.List;
import java.util.ArrayList;

public class ntnustudies_Course  {

    private float credtis;
    private String type;
    private String level;
    private String name;
    private String code;
    private String semesters;



    public ntnustudies_Course(
        float credtis,        String type,        String level,        String name,        String code,        String semesters    ) {
        this.credtis = credtis;
        this.type = type;
        this.level = level;
        this.name = name;
        this.code = code;
        this.semesters = semesters;
    }


    public float getCredtis() {
        return credtis;
    }

    public void setCredtis(float credtis) {
        this.credtis = credtis;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public String getSemesters() {
        return semesters;
    }

    public void setSemesters(String semesters) {
        this.semesters = semesters;
    }


}