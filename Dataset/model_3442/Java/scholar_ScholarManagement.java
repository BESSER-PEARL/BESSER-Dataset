





import java.util.List;
import java.util.ArrayList;

public class scholar_ScholarManagement  {






    private List<scholar_Teacher> scholar_teachers;




    private List<scholar_Lecture> scholar_lectures;




    private List<scholar_Student> scholar_students;




    private List<scholar_Discipline> scholar_disciplines;


    public scholar_ScholarManagement(
    ) {
        this.scholar_teachers = new ArrayList<>();
        this.scholar_lectures = new ArrayList<>();
        this.scholar_students = new ArrayList<>();
        this.scholar_disciplines = new ArrayList<>();
    }

    public scholar_ScholarManagement(
        ArrayList<scholar_Teacher> scholar_teachers,        ArrayList<scholar_Lecture> scholar_lectures,        ArrayList<scholar_Student> scholar_students,        ArrayList<scholar_Discipline> scholar_disciplines    ) {
        this.scholar_teachers = scholar_teachers;
        this.scholar_lectures = scholar_lectures;
        this.scholar_students = scholar_students;
        this.scholar_disciplines = scholar_disciplines;
    }


    public List<scholar_Teacher> getScholar_teachers() {
        return scholar_teachers;
    }

    public void addScholar_teacher(Scholar_teacher scholar_teacher) {
        this.scholar_teachers.add(scholar_teacher);
    }
    public List<scholar_Lecture> getScholar_lectures() {
        return scholar_lectures;
    }

    public void addScholar_lecture(Scholar_lecture scholar_lecture) {
        this.scholar_lectures.add(scholar_lecture);
    }
    public List<scholar_Student> getScholar_students() {
        return scholar_students;
    }

    public void addScholar_student(Scholar_student scholar_student) {
        this.scholar_students.add(scholar_student);
    }
    public List<scholar_Discipline> getScholar_disciplines() {
        return scholar_disciplines;
    }

    public void addScholar_discipline(Scholar_discipline scholar_discipline) {
        this.scholar_disciplines.add(scholar_discipline);
    }

}