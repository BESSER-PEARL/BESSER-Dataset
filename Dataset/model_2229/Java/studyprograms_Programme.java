





import java.util.List;
import java.util.ArrayList;

public class studyprograms_Programme  {

    private String code;
    private String name;
    private int startYear;
    private int duration;



    public studyprograms_Programme(
        String code,        String name,        int startYear,        int duration    ) {
        this.code = code;
        this.name = name;
        this.startYear = startYear;
        this.duration = duration;
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
    public int getStartyear() {
        return startYear;
    }

    public void setStartyear(int startYear) {
        this.startYear = startYear;
    }
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }


}