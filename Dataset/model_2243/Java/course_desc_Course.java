





import java.util.List;
import java.util.ArrayList;

public class course_desc_Course  {

    private String Code;
    private String Credits;
    private String name;
    private String Content;





    private course_desc_StudyProgram course_desc_studyprogram;




    private course_desc_Univ course_desc_univ;


    public course_desc_Course(
        String Code,        String Credits,        String name,        String Content    ) {
        this.Code = Code;
        this.Credits = Credits;
        this.name = name;
        this.Content = Content;
    }


    public String getCode() {
        return Code;
    }

    public void setCode(String Code) {
        this.Code = Code;
    }
    public String getCredits() {
        return Credits;
    }

    public void setCredits(String Credits) {
        this.Credits = Credits;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getContent() {
        return Content;
    }

    public void setContent(String Content) {
        this.Content = Content;
    }

    public course_desc_StudyProgram getCourse_desc_studyprogram() {
        return course_desc_studyprogram;
    }

    public void setCourse_desc_studyprogram(course_desc_StudyProgram course_desc_studyprogram) {
        this.course_desc_studyprogram = course_desc_studyprogram;
    }
    public course_desc_Univ getCourse_desc_univ() {
        return course_desc_univ;
    }

    public void setCourse_desc_univ(course_desc_Univ course_desc_univ) {
        this.course_desc_univ = course_desc_univ;
    }

}