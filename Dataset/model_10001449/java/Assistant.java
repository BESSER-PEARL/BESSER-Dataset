





import java.util.List;
import java.util.ArrayList;

public class Assistant  {

    private String CNIC;
    private String name;





    private List<Patients> patientss;




    private List<Appointment> appointments;




    private Doctor doctor;


    public Assistant(
        String CNIC,        String name    ) {
        this.CNIC = CNIC;
        this.name = name;
        this.patientss = new ArrayList<>();
        this.appointments = new ArrayList<>();
    }

    public Assistant(
        String CNIC,        String name        ArrayList<Patients> patientss,        ArrayList<Appointment> appointments    ) {
        this.CNIC = CNIC;
        this.name = name;
        this.patientss = patientss;
        this.appointments = appointments;
    }

    public String getCnic() {
        return CNIC;
    }

    public void setCnic(String CNIC) {
        this.CNIC = CNIC;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Patients> getPatientss() {
        return patientss;
    }

    public void addPatients(Patients patients) {
        this.patientss.add(patients);
    }
    public List<Appointment> getAppointments() {
        return appointments;
    }

    public void addAppointment(Appointment appointment) {
        this.appointments.add(appointment);
    }
    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

}