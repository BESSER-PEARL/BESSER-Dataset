





import java.util.List;
import java.util.ArrayList;

public class Database  {

    private None Grades;
    private None Accounts;
    private None Materials;
    private None Schedules;





    private Student student;




    private User user;




    private List<Teacher> teachers;


    public Database(
        None Grades,        None Accounts,        None Materials,        None Schedules    ) {
        this.Grades = Grades;
        this.Accounts = Accounts;
        this.Materials = Materials;
        this.Schedules = Schedules;
        this.teachers = new ArrayList<>();
    }

    public Database(
        None Grades,        None Accounts,        None Materials,        None Schedules        ArrayList<Teacher> teachers    ) {
        this.Grades = Grades;
        this.Accounts = Accounts;
        this.Materials = Materials;
        this.Schedules = Schedules;
        this.teachers = teachers;
    }

    public None getGrades() {
        return Grades;
    }

    public void setGrades(None Grades) {
        this.Grades = Grades;
    }
    public None getAccounts() {
        return Accounts;
    }

    public void setAccounts(None Accounts) {
        this.Accounts = Accounts;
    }
    public None getMaterials() {
        return Materials;
    }

    public void setMaterials(None Materials) {
        this.Materials = Materials;
    }
    public None getSchedules() {
        return Schedules;
    }

    public void setSchedules(None Schedules) {
        this.Schedules = Schedules;
    }

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }
    public List<Teacher> getTeachers() {
        return teachers;
    }

    public void addTeacher(Teacher teacher) {
        this.teachers.add(teacher);
    }

}