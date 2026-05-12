





import java.util.List;
import java.util.ArrayList;

public class RegularDoctor  {






    private List<Appointment> appointments;


    public RegularDoctor(
    ) {
        this.appointments = new ArrayList<>();
    }

    public RegularDoctor(
        ArrayList<Appointment> appointments    ) {
        this.appointments = appointments;
    }


    public List<Appointment> getAppointments() {
        return appointments;
    }

    public void addAppointment(Appointment appointment) {
        this.appointments.add(appointment);
    }

}