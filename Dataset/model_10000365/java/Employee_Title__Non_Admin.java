





import java.util.List;
import java.util.ArrayList;

public class Employee_Title__Non_Admin  {

    private None Teacher;
    private String Work_Study;
    private None Assistant_Teacher;
    private None Cook;
    private String Community_Service;
    private None Maintenance;





    private Employee_DB employee_db;


    public Employee_Title__Non_Admin(
        None Teacher,        String Work_Study,        None Assistant_Teacher,        None Cook,        String Community_Service,        None Maintenance    ) {
        this.Teacher = Teacher;
        this.Work_Study = Work_Study;
        this.Assistant_Teacher = Assistant_Teacher;
        this.Cook = Cook;
        this.Community_Service = Community_Service;
        this.Maintenance = Maintenance;
    }


    public None getTeacher() {
        return Teacher;
    }

    public void setTeacher(None Teacher) {
        this.Teacher = Teacher;
    }
    public String getWork_study() {
        return Work_Study;
    }

    public void setWork_study(String Work_Study) {
        this.Work_Study = Work_Study;
    }
    public None getAssistant_teacher() {
        return Assistant_Teacher;
    }

    public void setAssistant_teacher(None Assistant_Teacher) {
        this.Assistant_Teacher = Assistant_Teacher;
    }
    public None getCook() {
        return Cook;
    }

    public void setCook(None Cook) {
        this.Cook = Cook;
    }
    public String getCommunity_service() {
        return Community_Service;
    }

    public void setCommunity_service(String Community_Service) {
        this.Community_Service = Community_Service;
    }
    public None getMaintenance() {
        return Maintenance;
    }

    public void setMaintenance(None Maintenance) {
        this.Maintenance = Maintenance;
    }

    public Employee_DB getEmployee_db() {
        return employee_db;
    }

    public void setEmployee_db(Employee_DB employee_db) {
        this.employee_db = employee_db;
    }

}