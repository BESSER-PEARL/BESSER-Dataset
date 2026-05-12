





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String Languages;
    private String Joined;
    private String Education;
    private String Certification;





    private List<Hospital> hospitals;


    public Staff(
        String Languages,        String Joined,        String Education,        String Certification    ) {
        this.Languages = Languages;
        this.Joined = Joined;
        this.Education = Education;
        this.Certification = Certification;
        this.hospitals = new ArrayList<>();
    }

    public Staff(
        String Languages,        String Joined,        String Education,        String Certification        ArrayList<Hospital> hospitals    ) {
        this.Languages = Languages;
        this.Joined = Joined;
        this.Education = Education;
        this.Certification = Certification;
        this.hospitals = hospitals;
    }

    public String getLanguages() {
        return Languages;
    }

    public void setLanguages(String Languages) {
        this.Languages = Languages;
    }
    public String getJoined() {
        return Joined;
    }

    public void setJoined(String Joined) {
        this.Joined = Joined;
    }
    public String getEducation() {
        return Education;
    }

    public void setEducation(String Education) {
        this.Education = Education;
    }
    public String getCertification() {
        return Certification;
    }

    public void setCertification(String Certification) {
        this.Certification = Certification;
    }

    public List<Hospital> getHospitals() {
        return hospitals;
    }

    public void addHospital(Hospital hospital) {
        this.hospitals.add(hospital);
    }

}