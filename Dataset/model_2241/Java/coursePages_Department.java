





import java.util.List;
import java.util.ArrayList;

public class coursePages_Department  {

    private String phoneNummber;
    private String email;
    private String departmentName;





    private List<coursePages_Employee> coursepages_employees;




    private List<coursePages_StudyPrograms> coursepages_studyprogramss;




    private coursePages_StudyPrograms coursepages_studyprograms;




    private coursePages_Employee coursepages_employee;




    private List<coursePages_Course> coursepages_courses;


    public coursePages_Department(
        String phoneNummber,        String email,        String departmentName    ) {
        this.phoneNummber = phoneNummber;
        this.email = email;
        this.departmentName = departmentName;
        this.coursepages_employees = new ArrayList<>();
        this.coursepages_studyprogramss = new ArrayList<>();
        this.coursepages_courses = new ArrayList<>();
    }

    public coursePages_Department(
        String phoneNummber,        String email,        String departmentName        ArrayList<coursePages_Employee> coursepages_employees,        ArrayList<coursePages_StudyPrograms> coursepages_studyprogramss,        ArrayList<coursePages_Course> coursepages_courses    ) {
        this.phoneNummber = phoneNummber;
        this.email = email;
        this.departmentName = departmentName;
        this.coursepages_employees = coursepages_employees;
        this.coursepages_studyprogramss = coursepages_studyprogramss;
        this.coursepages_courses = coursepages_courses;
    }

    public String getPhonenummber() {
        return phoneNummber;
    }

    public void setPhonenummber(String phoneNummber) {
        this.phoneNummber = phoneNummber;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getDepartmentname() {
        return departmentName;
    }

    public void setDepartmentname(String departmentName) {
        this.departmentName = departmentName;
    }

    public List<coursePages_Employee> getCoursepages_employees() {
        return coursepages_employees;
    }

    public void addCoursepages_employee(Coursepages_employee coursepages_employee) {
        this.coursepages_employees.add(coursepages_employee);
    }
    public List<coursePages_StudyPrograms> getCoursepages_studyprogramss() {
        return coursepages_studyprogramss;
    }

    public void addCoursepages_studyprograms(Coursepages_studyprograms coursepages_studyprograms) {
        this.coursepages_studyprogramss.add(coursepages_studyprograms);
    }
    public coursePages_StudyPrograms getCoursepages_studyprograms() {
        return coursepages_studyprograms;
    }

    public void setCoursepages_studyprograms(coursePages_StudyPrograms coursepages_studyprograms) {
        this.coursepages_studyprograms = coursepages_studyprograms;
    }
    public coursePages_Employee getCoursepages_employee() {
        return coursepages_employee;
    }

    public void setCoursepages_employee(coursePages_Employee coursepages_employee) {
        this.coursepages_employee = coursepages_employee;
    }
    public List<coursePages_Course> getCoursepages_courses() {
        return coursepages_courses;
    }

    public void addCoursepages_course(Coursepages_course coursepages_course) {
        this.coursepages_courses.add(coursepages_course);
    }

}