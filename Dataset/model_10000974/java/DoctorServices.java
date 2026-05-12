





import java.util.List;
import java.util.ArrayList;

public class DoctorServices  {

    private int ServiceId;
    private String ServiceDetails;
    private String SId;
    private String ServicePrice;
    private String ServiceName;





    private List<Appointment> appointments;


    public DoctorServices(
        int ServiceId,        String ServiceDetails,        String SId,        String ServicePrice,        String ServiceName    ) {
        this.ServiceId = ServiceId;
        this.ServiceDetails = ServiceDetails;
        this.SId = SId;
        this.ServicePrice = ServicePrice;
        this.ServiceName = ServiceName;
        this.appointments = new ArrayList<>();
    }

    public DoctorServices(
        int ServiceId,        String ServiceDetails,        String SId,        String ServicePrice,        String ServiceName        ArrayList<Appointment> appointments    ) {
        this.ServiceId = ServiceId;
        this.ServiceDetails = ServiceDetails;
        this.SId = SId;
        this.ServicePrice = ServicePrice;
        this.ServiceName = ServiceName;
        this.appointments = appointments;
    }

    public int getServiceid() {
        return ServiceId;
    }

    public void setServiceid(int ServiceId) {
        this.ServiceId = ServiceId;
    }
    public String getServicedetails() {
        return ServiceDetails;
    }

    public void setServicedetails(String ServiceDetails) {
        this.ServiceDetails = ServiceDetails;
    }
    public String getSid() {
        return SId;
    }

    public void setSid(String SId) {
        this.SId = SId;
    }
    public String getServiceprice() {
        return ServicePrice;
    }

    public void setServiceprice(String ServicePrice) {
        this.ServicePrice = ServicePrice;
    }
    public String getServicename() {
        return ServiceName;
    }

    public void setServicename(String ServiceName) {
        this.ServiceName = ServiceName;
    }

    public List<Appointment> getAppointments() {
        return appointments;
    }

    public void addAppointment(Appointment appointment) {
        this.appointments.add(appointment);
    }

}