





import java.util.List;
import java.util.ArrayList;

public class Database  {

    private None Accounts;
    private None Schedules;
    private None Grades;
    private None Materials;





    private Student student;




    private User user;




    private List<Teacher> teachers;


    public Database(
        None Accounts,        None Schedules,        None Grades,        None Materials    ) {
        this.Accounts = Accounts;
        this.Schedules = Schedules;
        this.Grades = Grades;
        this.Materials = Materials;
        this.teachers = new ArrayList<>();
    }

    public Database(
        None Accounts,        None Schedules,        None Grades,        None Materials        ArrayList<Teacher> teachers    ) {
        this.Accounts = Accounts;
        this.Schedules = Schedules;
        this.Grades = Grades;
        this.Materials = Materials;
        this.teachers = teachers;
    }

    public None getAccounts() {
        return Accounts;
    }

    public void setAccounts(None Accounts) {
        this.Accounts = Accounts;
    }
    public None getSchedules() {
        return Schedules;
    }

    public void setSchedules(None Schedules) {
        this.Schedules = Schedules;
    }
    public None getGrades() {
        return Grades;
    }

    public void setGrades(None Grades) {
        this.Grades = Grades;
    }
    public None getMaterials() {
        return Materials;
    }

    public void setMaterials(None Materials) {
        this.Materials = Materials;
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