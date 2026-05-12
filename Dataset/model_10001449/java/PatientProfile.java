





import java.util.List;
import java.util.ArrayList;

public class PatientProfile  {

    private String name;
    private String appointment;





    private Receptionist receptionist;


    public PatientProfile(
        String name,        String appointment    ) {
        this.name = name;
        this.appointment = appointment;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAppointment() {
        return appointment;
    }

    public void setAppointment(String appointment) {
        this.appointment = appointment;
    }

    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }

}