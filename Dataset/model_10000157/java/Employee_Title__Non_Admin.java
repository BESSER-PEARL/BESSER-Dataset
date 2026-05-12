





import java.util.List;
import java.util.ArrayList;

public class Employee_Title__Non_Admin  {

    private String Work_Study;
    private None Cook;
    private None Teacher;
    private None Assistant_Teacher;
    private String Community_Service;
    private None Maintenance;



    public Employee_Title__Non_Admin(
        String Work_Study,        None Cook,        None Teacher,        None Assistant_Teacher,        String Community_Service,        None Maintenance    ) {
        this.Work_Study = Work_Study;
        this.Cook = Cook;
        this.Teacher = Teacher;
        this.Assistant_Teacher = Assistant_Teacher;
        this.Community_Service = Community_Service;
        this.Maintenance = Maintenance;
    }


    public String getWork_study() {
        return Work_Study;
    }

    public void setWork_study(String Work_Study) {
        this.Work_Study = Work_Study;
    }
    public None getCook() {
        return Cook;
    }

    public void setCook(None Cook) {
        this.Cook = Cook;
    }
    public None getTeacher() {
        return Teacher;
    }

    public void setTeacher(None Teacher) {
        this.Teacher = Teacher;
    }
    public None getAssistant_teacher() {
        return Assistant_Teacher;
    }

    public void setAssistant_teacher(None Assistant_Teacher) {
        this.Assistant_Teacher = Assistant_Teacher;
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


}