





import java.util.List;
import java.util.ArrayList;

public class Database  {

    private None Materials;
    private None Schedules;
    private None Accounts;
    private None Grades;





    private Student student;




    private User user;




    private List<Teacher> teachers;


    public Database(
        None Materials,        None Schedules,        None Accounts,        None Grades    ) {
        this.Materials = Materials;
        this.Schedules = Schedules;
        this.Accounts = Accounts;
        this.Grades = Grades;
        this.teachers = new ArrayList<>();
    }

    public Database(
        None Materials,        None Schedules,        None Accounts,        None Grades        ArrayList<Teacher> teachers    ) {
        this.Materials = Materials;
        this.Schedules = Schedules;
        this.Accounts = Accounts;
        this.Grades = Grades;
        this.teachers = teachers;
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
    public None getAccounts() {
        return Accounts;
    }

    public void setAccounts(None Accounts) {
        this.Accounts = Accounts;
    }
    public None getGrades() {
        return Grades;
    }

    public void setGrades(None Grades) {
        this.Grades = Grades;
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