





import java.util.List;
import java.util.ArrayList;

public class course  {

    private int course_id;
    private String course_preq;
    private String course_name;
    private int credit_hours;





    private List<Person> persons;




    private List<student> students;




    private List<Admin> admins;


    public course(
        int course_id,        String course_preq,        String course_name,        int credit_hours    ) {
        this.course_id = course_id;
        this.course_preq = course_preq;
        this.course_name = course_name;
        this.credit_hours = credit_hours;
        this.persons = new ArrayList<>();
        this.students = new ArrayList<>();
        this.admins = new ArrayList<>();
    }

    public course(
        int course_id,        String course_preq,        String course_name,        int credit_hours        ArrayList<Person> persons,        ArrayList<student> students,        ArrayList<Admin> admins    ) {
        this.course_id = course_id;
        this.course_preq = course_preq;
        this.course_name = course_name;
        this.credit_hours = credit_hours;
        this.persons = persons;
        this.students = students;
        this.admins = admins;
    }

    public int getCourse_id() {
        return course_id;
    }

    public void setCourse_id(int course_id) {
        this.course_id = course_id;
    }
    public String getCourse_preq() {
        return course_preq;
    }

    public void setCourse_preq(String course_preq) {
        this.course_preq = course_preq;
    }
    public String getCourse_name() {
        return course_name;
    }

    public void setCourse_name(String course_name) {
        this.course_name = course_name;
    }
    public int getCredit_hours() {
        return credit_hours;
    }

    public void setCredit_hours(int credit_hours) {
        this.credit_hours = credit_hours;
    }

    public List<Person> getPersons() {
        return persons;
    }

    public void addPerson(Person person) {
        this.persons.add(person);
    }
    public List<student> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }
    public List<Admin> getAdmins() {
        return admins;
    }

    public void addAdmin(Admin admin) {
        this.admins.add(admin);
    }

}