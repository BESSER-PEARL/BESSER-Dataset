





import java.util.List;
import java.util.ArrayList;

public class tdt4250_Course  {

    private String level;
    private float study_points;
    private String code;
    private String name;





    private tdt4250_Student tdt4250_student;




    private tdt4250_StudyProgram tdt4250_studyprogram;




    private tdt4250_Specialisation tdt4250_specialisation;




    private tdt4250_Specialisation tdt4250_specialisation;


    public tdt4250_Course(
        String level,        float study_points,        String code,        String name    ) {
        this.level = level;
        this.study_points = study_points;
        this.code = code;
        this.name = name;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public float getStudy_points() {
        return study_points;
    }

    public void setStudy_points(float study_points) {
        this.study_points = study_points;
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
    public tdt4250_Specialisation getTdt4250_specialisation() {
        return tdt4250_specialisation;
    }

    public void setTdt4250_specialisation(tdt4250_Specialisation tdt4250_specialisation) {
        this.tdt4250_specialisation = tdt4250_specialisation;
    }
    public tdt4250_Specialisation getTdt4250_specialisation() {
        return tdt4250_specialisation;
    }

    public void setTdt4250_specialisation(tdt4250_Specialisation tdt4250_specialisation) {
        this.tdt4250_specialisation = tdt4250_specialisation;
    }

}