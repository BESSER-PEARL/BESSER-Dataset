





import java.util.List;
import java.util.ArrayList;

public class study_Programme  {

    private String name;
    private String code;
    private int duration;



    public study_Programme(
        String name,        String code,        int duration    ) {
        this.name = name;
        this.code = code;
        this.duration = duration;
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
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }


}