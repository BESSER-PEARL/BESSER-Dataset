





import java.util.List;
import java.util.ArrayList;

public class patient  {






    private List<junior_doctor> junior_doctors;




    private team team;




    private consultant_doctor consultant_doctor;


    public patient(
    ) {
        this.junior_doctors = new ArrayList<>();
    }

    public patient(
        ArrayList<junior_doctor> junior_doctors    ) {
        this.junior_doctors = junior_doctors;
    }


    public List<junior_doctor> getJunior_doctors() {
        return junior_doctors;
    }

    public void addJunior_doctor(Junior_doctor junior_doctor) {
        this.junior_doctors.add(junior_doctor);
    }
    public team getTeam() {
        return team;
    }

    public void setTeam(team team) {
        this.team = team;
    }
    public consultant_doctor getConsultant_doctor() {
        return consultant_doctor;
    }

    public void setConsultant_doctor(consultant_doctor consultant_doctor) {
        this.consultant_doctor = consultant_doctor;
    }

}