





import java.util.List;
import java.util.ArrayList;

public class Database  {

    private None Schedules;
    private None Materials;
    private None Grades;
    private None Accounts;





    private List<Profesor> profesors;




    private Usuario usuario;




    private Student student;


    public Database(
        None Schedules,        None Materials,        None Grades,        None Accounts    ) {
        this.Schedules = Schedules;
        this.Materials = Materials;
        this.Grades = Grades;
        this.Accounts = Accounts;
        this.profesors = new ArrayList<>();
    }

    public Database(
        None Schedules,        None Materials,        None Grades,        None Accounts        ArrayList<Profesor> profesors    ) {
        this.Schedules = Schedules;
        this.Materials = Materials;
        this.Grades = Grades;
        this.Accounts = Accounts;
        this.profesors = profesors;
    }

    public None getSchedules() {
        return Schedules;
    }

    public void setSchedules(None Schedules) {
        this.Schedules = Schedules;
    }
    public None getMaterials() {
        return Materials;
    }

    public void setMaterials(None Materials) {
        this.Materials = Materials;
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

    public List<Profesor> getProfesors() {
        return profesors;
    }

    public void addProfesor(Profesor profesor) {
        this.profesors.add(profesor);
    }
    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }
    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }

}