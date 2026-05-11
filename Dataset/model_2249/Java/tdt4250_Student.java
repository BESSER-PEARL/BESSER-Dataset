





import java.util.List;
import java.util.ArrayList;

public class tdt4250_Student  {

    private int studentID;
    private int current_semester;





    private tdt4250_StudyProgram tdt4250_studyprogram;


    public tdt4250_Student(
        int studentID,        int current_semester    ) {
        this.studentID = studentID;
        this.current_semester = current_semester;
    }


    public int getStudentid() {
        return studentID;
    }

    public void setStudentid(int studentID) {
        this.studentID = studentID;
    }
    public int getCurrent_semester() {
        return current_semester;
    }

    public void setCurrent_semester(int current_semester) {
        this.current_semester = current_semester;
    }

    public tdt4250_StudyProgram getTdt4250_studyprogram() {
        return tdt4250_studyprogram;
    }

    public void setTdt4250_studyprogram(tdt4250_StudyProgram tdt4250_studyprogram) {
        this.tdt4250_studyprogram = tdt4250_studyprogram;
    }

}