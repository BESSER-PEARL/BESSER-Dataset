




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class hairDressersRegSys_Service  {

    private String Name;
    private LocalDate Time;
    private String CostPerHour;
    private String Description;





    private List<hairDressersRegSys_Appointment> hairdressersregsys_appointments;


    public hairDressersRegSys_Service(
        String Name,        LocalDate Time,        String CostPerHour,        String Description    ) {
        this.Name = Name;
        this.Time = Time;
        this.CostPerHour = CostPerHour;
        this.Description = Description;
        this.hairdressersregsys_appointments = new ArrayList<>();
    }

    public hairDressersRegSys_Service(
        String Name,        LocalDate Time,        String CostPerHour,        String Description        ArrayList<hairDressersRegSys_Appointment> hairdressersregsys_appointments    ) {
        this.Name = Name;
        this.Time = Time;
        this.CostPerHour = CostPerHour;
        this.Description = Description;
        this.hairdressersregsys_appointments = hairdressersregsys_appointments;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public LocalDate getTime() {
        return Time;
    }

    public void setTime(LocalDate Time) {
        this.Time = Time;
    }
    public String getCostperhour() {
        return CostPerHour;
    }

    public void setCostperhour(String CostPerHour) {
        this.CostPerHour = CostPerHour;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }

    public List<hairDressersRegSys_Appointment> getHairdressersregsys_appointments() {
        return hairdressersregsys_appointments;
    }

    public void addHairdressersregsys_appointment(Hairdressersregsys_appointment hairdressersregsys_appointment) {
        this.hairdressersregsys_appointments.add(hairdressersregsys_appointment);
    }

}