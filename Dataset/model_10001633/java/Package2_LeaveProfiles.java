





import java.util.List;
import java.util.ArrayList;

public class Package2_LeaveProfiles  {

    private int id;
    private int anual;
    private int casual;
    private String name;





    private Package2_Employee package2_employee;


    public Package2_LeaveProfiles(
        int id,        int anual,        int casual,        String name    ) {
        this.id = id;
        this.anual = anual;
        this.casual = casual;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getAnual() {
        return anual;
    }

    public void setAnual(int anual) {
        this.anual = anual;
    }
    public int getCasual() {
        return casual;
    }

    public void setCasual(int casual) {
        this.casual = casual;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Package2_Employee getPackage2_employee() {
        return package2_employee;
    }

    public void setPackage2_employee(Package2_Employee package2_employee) {
        this.package2_employee = package2_employee;
    }

}