





import java.util.List;
import java.util.ArrayList;

public class HOD  {

    private String password;
    private String id;





    private List<STUDENT> students;




    private List<COUNSELLOR> counsellors;


    public HOD(
        String password,        String id    ) {
        this.password = password;
        this.id = id;
        this.students = new ArrayList<>();
        this.counsellors = new ArrayList<>();
    }

    public HOD(
        String password,        String id        ArrayList<STUDENT> students,        ArrayList<COUNSELLOR> counsellors    ) {
        this.password = password;
        this.id = id;
        this.students = students;
        this.counsellors = counsellors;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<STUDENT> getStudents() {
        return students;
    }

    public void addStudent(Student student) {
        this.students.add(student);
    }
    public List<COUNSELLOR> getCounsellors() {
        return counsellors;
    }

    public void addCounsellor(Counsellor counsellor) {
        this.counsellors.add(counsellor);
    }

}