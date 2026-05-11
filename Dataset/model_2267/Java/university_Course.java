





import java.util.List;
import java.util.ArrayList;

public class university_Course  {

    private int numberOfAttendants;
    private String name;
    private float gradeAverage;





    private List<university_Certificate> university_certificates;




    private university_Professor university_professor;




    private university_Professor university_professor;




    private university_University university_university;




    private university_Certificate university_certificate;


    public university_Course(
        int numberOfAttendants,        String name,        float gradeAverage    ) {
        this.numberOfAttendants = numberOfAttendants;
        this.name = name;
        this.gradeAverage = gradeAverage;
        this.university_certificates = new ArrayList<>();
    }

    public university_Course(
        int numberOfAttendants,        String name,        float gradeAverage        ArrayList<university_Certificate> university_certificates    ) {
        this.numberOfAttendants = numberOfAttendants;
        this.name = name;
        this.gradeAverage = gradeAverage;
        this.university_certificates = university_certificates;
    }

    public int getNumberofattendants() {
        return numberOfAttendants;
    }

    public void setNumberofattendants(int numberOfAttendants) {
        this.numberOfAttendants = numberOfAttendants;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getGradeaverage() {
        return gradeAverage;
    }

    public void setGradeaverage(float gradeAverage) {
        this.gradeAverage = gradeAverage;
    }

    public List<university_Certificate> getUniversity_certificates() {
        return university_certificates;
    }

    public void addUniversity_certificate(University_certificate university_certificate) {
        this.university_certificates.add(university_certificate);
    }
    public university_Professor getUniversity_professor() {
        return university_professor;
    }

    public void setUniversity_professor(university_Professor university_professor) {
        this.university_professor = university_professor;
    }
    public university_Professor getUniversity_professor() {
        return university_professor;
    }

    public void setUniversity_professor(university_Professor university_professor) {
        this.university_professor = university_professor;
    }
    public university_University getUniversity_university() {
        return university_university;
    }

    public void setUniversity_university(university_University university_university) {
        this.university_university = university_university;
    }
    public university_Certificate getUniversity_certificate() {
        return university_certificate;
    }

    public void setUniversity_certificate(university_Certificate university_certificate) {
        this.university_certificate = university_certificate;
    }

}