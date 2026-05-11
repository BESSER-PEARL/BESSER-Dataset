





import java.util.List;
import java.util.ArrayList;

public class hairDressersRegSys_Customer extends Person {

    private int CustomerId;





    private List<hairDressersRegSys_Appointment> hairdressersregsys_appointments;


    public hairDressersRegSys_Customer(
        int CustomerId    ) {
        super(
        );
        this.CustomerId = CustomerId;
        this.hairdressersregsys_appointments = new ArrayList<>();
    }

    public hairDressersRegSys_Customer(
        int CustomerId        ArrayList<hairDressersRegSys_Appointment> hairdressersregsys_appointments    ) {
        this.CustomerId = CustomerId;
        this.hairdressersregsys_appointments = hairdressersregsys_appointments;
    }

    public int getCustomerid() {
        return CustomerId;
    }

    public void setCustomerid(int CustomerId) {
        this.CustomerId = CustomerId;
    }

    public List<hairDressersRegSys_Appointment> getHairdressersregsys_appointments() {
        return hairdressersregsys_appointments;
    }

    public void addHairdressersregsys_appointment(Hairdressersregsys_appointment hairdressersregsys_appointment) {
        this.hairdressersregsys_appointments.add(hairdressersregsys_appointment);
    }

}