





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String Education;
    private String Languages;
    private String Certification;
    private String Joined;





    private List<Hospital> hospitals;


    public Staff(
        String Education,        String Languages,        String Certification,        String Joined    ) {
        this.Education = Education;
        this.Languages = Languages;
        this.Certification = Certification;
        this.Joined = Joined;
        this.hospitals = new ArrayList<>();
    }

    public Staff(
        String Education,        String Languages,        String Certification,        String Joined        ArrayList<Hospital> hospitals    ) {
        this.Education = Education;
        this.Languages = Languages;
        this.Certification = Certification;
        this.Joined = Joined;
        this.hospitals = hospitals;
    }

    public String getEducation() {
        return Education;
    }

    public void setEducation(String Education) {
        this.Education = Education;
    }
    public String getLanguages() {
        return Languages;
    }

    public void setLanguages(String Languages) {
        this.Languages = Languages;
    }
    public String getCertification() {
        return Certification;
    }

    public void setCertification(String Certification) {
        this.Certification = Certification;
    }
    public String getJoined() {
        return Joined;
    }

    public void setJoined(String Joined) {
        this.Joined = Joined;
    }

    public List<Hospital> getHospitals() {
        return hospitals;
    }

    public void addHospital(Hospital hospital) {
        this.hospitals.add(hospital);
    }

}