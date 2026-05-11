





import java.util.List;
import java.util.ArrayList;

public class tDT4250_asssignment1_2_Course  {

    private String Name;
    private String StartDate;
    private float Credits;
    private String ExamDate;
    private String Code;





    private tDT4250_asssignment1_2_Semester_Course tdt4250_asssignment1_2_semester_course;


    public tDT4250_asssignment1_2_Course(
        String Name,        String StartDate,        float Credits,        String ExamDate,        String Code    ) {
        this.Name = Name;
        this.StartDate = StartDate;
        this.Credits = Credits;
        this.ExamDate = ExamDate;
        this.Code = Code;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getStartdate() {
        return StartDate;
    }

    public void setStartdate(String StartDate) {
        this.StartDate = StartDate;
    }
    public float getCredits() {
        return Credits;
    }

    public void setCredits(float Credits) {
        this.Credits = Credits;
    }
    public String getExamdate() {
        return ExamDate;
    }

    public void setExamdate(String ExamDate) {
        this.ExamDate = ExamDate;
    }
    public String getCode() {
        return Code;
    }

    public void setCode(String Code) {
        this.Code = Code;
    }

    public tDT4250_asssignment1_2_Semester_Course getTdt4250_asssignment1_2_semester_course() {
        return tdt4250_asssignment1_2_semester_course;
    }

    public void setTdt4250_asssignment1_2_semester_course(tDT4250_asssignment1_2_Semester_Course tdt4250_asssignment1_2_semester_course) {
        this.tdt4250_asssignment1_2_semester_course = tdt4250_asssignment1_2_semester_course;
    }

}