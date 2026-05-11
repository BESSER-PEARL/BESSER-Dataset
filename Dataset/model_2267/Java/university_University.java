





import java.util.List;
import java.util.ArrayList;

public class university_University  {

    private int numberOfStudents;
    private float averageLength;
    private String name;





    private List<university_Certificate> university_certificates;




    private List<university_Professor> university_professors;


    public university_University(
        int numberOfStudents,        float averageLength,        String name    ) {
        this.numberOfStudents = numberOfStudents;
        this.averageLength = averageLength;
        this.name = name;
        this.university_certificates = new ArrayList<>();
        this.university_professors = new ArrayList<>();
    }

    public university_University(
        int numberOfStudents,        float averageLength,        String name        ArrayList<university_Certificate> university_certificates,        ArrayList<university_Professor> university_professors    ) {
        this.numberOfStudents = numberOfStudents;
        this.averageLength = averageLength;
        this.name = name;
        this.university_certificates = university_certificates;
        this.university_professors = university_professors;
    }

    public int getNumberofstudents() {
        return numberOfStudents;
    }

    public void setNumberofstudents(int numberOfStudents) {
        this.numberOfStudents = numberOfStudents;
    }
    public float getAveragelength() {
        return averageLength;
    }

    public void setAveragelength(float averageLength) {
        this.averageLength = averageLength;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<university_Certificate> getUniversity_certificates() {
        return university_certificates;
    }

    public void addUniversity_certificate(University_certificate university_certificate) {
        this.university_certificates.add(university_certificate);
    }
    public List<university_Professor> getUniversity_professors() {
        return university_professors;
    }

    public void addUniversity_professor(University_professor university_professor) {
        this.university_professors.add(university_professor);
    }

}