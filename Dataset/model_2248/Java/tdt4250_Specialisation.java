





import java.util.List;
import java.util.ArrayList;

public class tdt4250_Specialisation  {

    private String name;





    private tdt4250_Specialisation tdt4250_specialisation;




    private List<tdt4250_Student> tdt4250_students;




    private tdt4250_StudyProgram tdt4250_studyprogram;


    public tdt4250_Specialisation(
        String name    ) {
        this.name = name;
        this.tdt4250_students = new ArrayList<>();
    }

    public tdt4250_Specialisation(
        String name        ArrayList<tdt4250_Student> tdt4250_students    ) {
        this.name = name;
        this.tdt4250_students = tdt4250_students;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tdt4250_Specialisation getTdt4250_specialisation() {
        return tdt4250_specialisation;
    }

    public void setTdt4250_specialisation(tdt4250_Specialisation tdt4250_specialisation) {
        this.tdt4250_specialisation = tdt4250_specialisation;
    }
    public List<tdt4250_Student> getTdt4250_students() {
        return tdt4250_students;
    }

    public void addTdt4250_student(Tdt4250_student tdt4250_student) {
        this.tdt4250_students.add(tdt4250_student);
    }
    public tdt4250_StudyProgram getTdt4250_studyprogram() {
        return tdt4250_studyprogram;
    }

    public void setTdt4250_studyprogram(tdt4250_StudyProgram tdt4250_studyprogram) {
        this.tdt4250_studyprogram = tdt4250_studyprogram;
    }

}