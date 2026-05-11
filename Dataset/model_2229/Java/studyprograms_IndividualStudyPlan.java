





import java.util.List;
import java.util.ArrayList;

public class studyprograms_IndividualStudyPlan  {

    private String studentNo;





    private List<studyprograms_Semester> studyprograms_semesters;


    public studyprograms_IndividualStudyPlan(
        String studentNo    ) {
        this.studentNo = studentNo;
        this.studyprograms_semesters = new ArrayList<>();
    }

    public studyprograms_IndividualStudyPlan(
        String studentNo        ArrayList<studyprograms_Semester> studyprograms_semesters    ) {
        this.studentNo = studentNo;
        this.studyprograms_semesters = studyprograms_semesters;
    }

    public String getStudentno() {
        return studentNo;
    }

    public void setStudentno(String studentNo) {
        this.studentNo = studentNo;
    }

    public List<studyprograms_Semester> getStudyprograms_semesters() {
        return studyprograms_semesters;
    }

    public void addStudyprograms_semester(Studyprograms_semester studyprograms_semester) {
        this.studyprograms_semesters.add(studyprograms_semester);
    }

}