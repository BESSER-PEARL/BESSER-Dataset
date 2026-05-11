





import java.util.List;
import java.util.ArrayList;

public class study_StudyProgramme  {

    private int numYears;
    private String name;
    private String code;



    public study_StudyProgramme(
        int numYears,        String name,        String code    ) {
        this.numYears = numYears;
        this.name = name;
        this.code = code;
    }


    public int getNumyears() {
        return numYears;
    }

    public void setNumyears(int numYears) {
        this.numYears = numYears;
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


}