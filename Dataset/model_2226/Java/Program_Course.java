





import java.util.List;
import java.util.ArrayList;

public class Program_Course  {

    private String code;
    private String name;
    private float credit;





    private Program_SemesterCourse program_semestercourse;


    public Program_Course(
        String code,        String name,        float credit    ) {
        this.code = code;
        this.name = name;
        this.credit = credit;
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
    public float getCredit() {
        return credit;
    }

    public void setCredit(float credit) {
        this.credit = credit;
    }

    public Program_SemesterCourse getProgram_semestercourse() {
        return program_semestercourse;
    }

    public void setProgram_semestercourse(Program_SemesterCourse program_semestercourse) {
        this.program_semestercourse = program_semestercourse;
    }

}