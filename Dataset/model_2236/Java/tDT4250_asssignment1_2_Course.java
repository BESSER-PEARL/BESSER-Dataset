





import java.util.List;
import java.util.ArrayList;

public class tDT4250_asssignment1_2_Course  {

    private String StartDate;
    private float Credits;
    private String Name;
    private String ExamDate;
    private String Code;





    private tDT4250_asssignment1_2_Semester_Course tdt4250_asssignment1_2_semester_course;


    public tDT4250_asssignment1_2_Course(
        String StartDate,        float Credits,        String Name,        String ExamDate,        String Code    ) {
        this.StartDate = StartDate;
        this.Credits = Credits;
        this.Name = Name;
        this.ExamDate = ExamDate;
        this.Code = Code;
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
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
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