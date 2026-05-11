





import java.util.List;
import java.util.ArrayList;

public class university_Courses  {

    private String code;
    private float credits;
    private String name;



    public university_Courses(
        String code,        float credits,        String name    ) {
        this.code = code;
        this.credits = credits;
        this.name = name;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}