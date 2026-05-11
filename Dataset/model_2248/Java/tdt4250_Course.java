





import java.util.List;
import java.util.ArrayList;

public class tdt4250_Course  {

    private String name;
    private String semester;
    private String code;
    private float study_points;
    private String level;





    private tdt4250_Student tdt4250_student;




    private tdt4250_StudyProgram tdt4250_studyprogram;


    public tdt4250_Course(
        String name,        String semester,        String code,        float study_points,        String level    ) {
        this.name = name;
        this.semester = semester;
        this.code = code;
        this.study_points = study_points;
        this.level = level;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSemester() {
        return semester;
    }

    public void setSemester(String semester) {
        this.semester = semester;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public float getStudy_points() {
        return study_points;
    }

    public void setStudy_points(float study_points) {
        this.study_points = study_points;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }

    public tdt4250_Student getTdt4250_student() {
        return tdt4250_student;
    }

    public void setTdt4250_student(tdt4250_Student tdt4250_student) {
        this.tdt4250_student = tdt4250_student;
    }
    public tdt4250_StudyProgram getTdt4250_studyprogram() {
        return tdt4250_studyprogram;
    }

    public void setTdt4250_studyprogram(tdt4250_StudyProgram tdt4250_studyprogram) {
        this.tdt4250_studyprogram = tdt4250_studyprogram;
    }

}