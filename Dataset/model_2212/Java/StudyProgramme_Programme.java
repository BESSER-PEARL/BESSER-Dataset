





import java.util.List;
import java.util.ArrayList;

public class StudyProgramme_Programme  {

    private String code;
    private int duration;
    private String name;



    public StudyProgramme_Programme(
        String code,        int duration,        String name    ) {
        this.code = code;
        this.duration = duration;
        this.name = name;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}