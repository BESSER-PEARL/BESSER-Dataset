





import java.util.List;
import java.util.ArrayList;

public class university_Student  {

    private String MNR;
    private int semester;





    private university_University university_university;




    private List<university_Certificate> university_certificates;




    private university_Certificate university_certificate;


    public university_Student(
        String MNR,        int semester    ) {
        this.MNR = MNR;
        this.semester = semester;
        this.university_certificates = new ArrayList<>();
    }

    public university_Student(
        String MNR,        int semester        ArrayList<university_Certificate> university_certificates    ) {
        this.MNR = MNR;
        this.semester = semester;
        this.university_certificates = university_certificates;
    }

    public String getMnr() {
        return MNR;
    }

    public void setMnr(String MNR) {
        this.MNR = MNR;
    }
    public int getSemester() {
        return semester;
    }

    public void setSemester(int semester) {
        this.semester = semester;
    }

    public university_University getUniversity_university() {
        return university_university;
    }

    public void setUniversity_university(university_University university_university) {
        this.university_university = university_university;
    }
    public List<university_Certificate> getUniversity_certificates() {
        return university_certificates;
    }

    public void addUniversity_certificate(University_certificate university_certificate) {
        this.university_certificates.add(university_certificate);
    }
    public university_Certificate getUniversity_certificate() {
        return university_certificate;
    }

    public void setUniversity_certificate(university_Certificate university_certificate) {
        this.university_certificate = university_certificate;
    }

}