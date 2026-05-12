





import java.util.List;
import java.util.ArrayList;

public class attendance_manager  {

    private String student_names;
    private String identify_students;
    private String Excuse_of_Absenties;





    private List<students> studentss;




    private teacher teacher;




    private Parents parents;


    public attendance_manager(
        String student_names,        String identify_students,        String Excuse_of_Absenties    ) {
        this.student_names = student_names;
        this.identify_students = identify_students;
        this.Excuse_of_Absenties = Excuse_of_Absenties;
        this.studentss = new ArrayList<>();
    }

    public attendance_manager(
        String student_names,        String identify_students,        String Excuse_of_Absenties        ArrayList<students> studentss    ) {
        this.student_names = student_names;
        this.identify_students = identify_students;
        this.Excuse_of_Absenties = Excuse_of_Absenties;
        this.studentss = studentss;
    }

    public String getStudent_names() {
        return student_names;
    }

    public void setStudent_names(String student_names) {
        this.student_names = student_names;
    }
    public String getIdentify_students() {
        return identify_students;
    }

    public void setIdentify_students(String identify_students) {
        this.identify_students = identify_students;
    }
    public String getExcuse_of_absenties() {
        return Excuse_of_Absenties;
    }

    public void setExcuse_of_absenties(String Excuse_of_Absenties) {
        this.Excuse_of_Absenties = Excuse_of_Absenties;
    }

    public List<students> getStudentss() {
        return studentss;
    }

    public void addStudents(Students students) {
        this.studentss.add(students);
    }
    public teacher getTeacher() {
        return teacher;
    }

    public void setTeacher(teacher teacher) {
        this.teacher = teacher;
    }
    public Parents getParents() {
        return parents;
    }

    public void setParents(Parents parents) {
        this.parents = parents;
    }

}