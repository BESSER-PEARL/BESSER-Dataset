





import java.util.List;
import java.util.ArrayList;

public class reservationsystem_Crew extends Person {

    private String employeeId;





    private reservationsystem_Crew reservationsystem_crew;


    public reservationsystem_Crew(
        String employeeId    ) {
        super(
        );
        this.employeeId = employeeId;
    }


    public String getEmployeeid() {
        return employeeId;
    }

    public void setEmployeeid(String employeeId) {
        this.employeeId = employeeId;
    }

    public reservationsystem_Crew getReservationsystem_crew() {
        return reservationsystem_crew;
    }

    public void setReservationsystem_crew(reservationsystem_Crew reservationsystem_crew) {
        this.reservationsystem_crew = reservationsystem_crew;
    }

}