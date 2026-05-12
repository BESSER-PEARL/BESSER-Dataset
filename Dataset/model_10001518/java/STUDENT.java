





import java.util.List;
import java.util.ArrayList;

public class STUDENT  {

    private String EMAIL_ID;
    private String QUALIFICATION;
    private String NAME;
    private String COURSE;
    private int CONTACT_NO;
    private int STUD_ID;





    private ADMIN admin;




    private List<EMPLOYEE> employees;


    public STUDENT(
        String EMAIL_ID,        String QUALIFICATION,        String NAME,        String COURSE,        int CONTACT_NO,        int STUD_ID    ) {
        this.EMAIL_ID = EMAIL_ID;
        this.QUALIFICATION = QUALIFICATION;
        this.NAME = NAME;
        this.COURSE = COURSE;
        this.CONTACT_NO = CONTACT_NO;
        this.STUD_ID = STUD_ID;
        this.employees = new ArrayList<>();
    }

    public STUDENT(
        String EMAIL_ID,        String QUALIFICATION,        String NAME,        String COURSE,        int CONTACT_NO,        int STUD_ID        ArrayList<EMPLOYEE> employees    ) {
        this.EMAIL_ID = EMAIL_ID;
        this.QUALIFICATION = QUALIFICATION;
        this.NAME = NAME;
        this.COURSE = COURSE;
        this.CONTACT_NO = CONTACT_NO;
        this.STUD_ID = STUD_ID;
        this.employees = employees;
    }

    public String getEmail_id() {
        return EMAIL_ID;
    }

    public void setEmail_id(String EMAIL_ID) {
        this.EMAIL_ID = EMAIL_ID;
    }
    public String getQualification() {
        return QUALIFICATION;
    }

    public void setQualification(String QUALIFICATION) {
        this.QUALIFICATION = QUALIFICATION;
    }
    public String getName() {
        return NAME;
    }

    public void setName(String NAME) {
        this.NAME = NAME;
    }
    public String getCourse() {
        return COURSE;
    }

    public void setCourse(String COURSE) {
        this.COURSE = COURSE;
    }
    public int getContact_no() {
        return CONTACT_NO;
    }

    public void setContact_no(int CONTACT_NO) {
        this.CONTACT_NO = CONTACT_NO;
    }
    public int getStud_id() {
        return STUD_ID;
    }

    public void setStud_id(int STUD_ID) {
        this.STUD_ID = STUD_ID;
    }

    public ADMIN getAdmin() {
        return admin;
    }

    public void setAdmin(ADMIN admin) {
        this.admin = admin;
    }
    public List<EMPLOYEE> getEmployees() {
        return employees;
    }

    public void addEmployee(Employee employee) {
        this.employees.add(employee);
    }

}