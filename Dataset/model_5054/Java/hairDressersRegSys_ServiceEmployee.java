





import java.util.List;
import java.util.ArrayList;

public class hairDressersRegSys_ServiceEmployee extends Person {

    private int EmployeeId;
    private String Role;





    private List<hairDressersRegSys_Appointment> hairdressersregsys_appointments;


    public hairDressersRegSys_ServiceEmployee(
        int EmployeeId,        String Role    ) {
        super(
        );
        this.EmployeeId = EmployeeId;
        this.Role = Role;
        this.hairdressersregsys_appointments = new ArrayList<>();
    }

    public hairDressersRegSys_ServiceEmployee(
        int EmployeeId,        String Role        ArrayList<hairDressersRegSys_Appointment> hairdressersregsys_appointments    ) {
        this.EmployeeId = EmployeeId;
        this.Role = Role;
        this.hairdressersregsys_appointments = hairdressersregsys_appointments;
    }

    public int getEmployeeid() {
        return EmployeeId;
    }

    public void setEmployeeid(int EmployeeId) {
        this.EmployeeId = EmployeeId;
    }
    public String getRole() {
        return Role;
    }

    public void setRole(String Role) {
        this.Role = Role;
    }

    public List<hairDressersRegSys_Appointment> getHairdressersregsys_appointments() {
        return hairdressersregsys_appointments;
    }

    public void addHairdressersregsys_appointment(Hairdressersregsys_appointment hairdressersregsys_appointment) {
        this.hairdressersregsys_appointments.add(hairdressersregsys_appointment);
    }

}