





import java.util.List;
import java.util.ArrayList;

public class oving4_Course  {

    private String content;
    private float credits;
    private String code;
    private String name;
    private String examStartDate;
    private String examEndDate;





    private oving4_StudyProgram oving4_studyprogram;




    private oving4_Department oving4_department;




    private oving4_StudyProgram oving4_studyprogram;


    public oving4_Course(
        String content,        float credits,        String code,        String name,        String examStartDate,        String examEndDate    ) {
        this.content = content;
        this.credits = credits;
        this.code = code;
        this.name = name;
        this.examStartDate = examStartDate;
        this.examEndDate = examEndDate;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
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
    public String getExamstartdate() {
        return examStartDate;
    }

    public void setExamstartdate(String examStartDate) {
        this.examStartDate = examStartDate;
    }
    public String getExamenddate() {
        return examEndDate;
    }

    public void setExamenddate(String examEndDate) {
        this.examEndDate = examEndDate;
    }

    public oving4_StudyProgram getOving4_studyprogram() {
        return oving4_studyprogram;
    }

    public void setOving4_studyprogram(oving4_StudyProgram oving4_studyprogram) {
        this.oving4_studyprogram = oving4_studyprogram;
    }
    public oving4_Department getOving4_department() {
        return oving4_department;
    }

    public void setOving4_department(oving4_Department oving4_department) {
        this.oving4_department = oving4_department;
    }
    public oving4_StudyProgram getOving4_studyprogram() {
        return oving4_studyprogram;
    }

    public void setOving4_studyprogram(oving4_StudyProgram oving4_studyprogram) {
        this.oving4_studyprogram = oving4_studyprogram;
    }

}