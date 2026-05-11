





import java.util.List;
import java.util.ArrayList;

public class studyprogramme_Semester  {

    private int semesterNumber;





    private studyprogramme_SemesterContainer studyprogramme_semestercontainer;




    private studyprogramme_University studyprogramme_university;




    private List<studyprogramme_CourseSlot> studyprogramme_courseslots;


    public studyprogramme_Semester(
        int semesterNumber    ) {
        this.semesterNumber = semesterNumber;
        this.studyprogramme_courseslots = new ArrayList<>();
    }

    public studyprogramme_Semester(
        int semesterNumber        ArrayList<studyprogramme_CourseSlot> studyprogramme_courseslots    ) {
        this.semesterNumber = semesterNumber;
        this.studyprogramme_courseslots = studyprogramme_courseslots;
    }

    public int getSemesternumber() {
        return semesterNumber;
    }

    public void setSemesternumber(int semesterNumber) {
        this.semesterNumber = semesterNumber;
    }

    public studyprogramme_SemesterContainer getStudyprogramme_semestercontainer() {
        return studyprogramme_semestercontainer;
    }

    public void setStudyprogramme_semestercontainer(studyprogramme_SemesterContainer studyprogramme_semestercontainer) {
        this.studyprogramme_semestercontainer = studyprogramme_semestercontainer;
    }
    public studyprogramme_University getStudyprogramme_university() {
        return studyprogramme_university;
    }

    public void setStudyprogramme_university(studyprogramme_University studyprogramme_university) {
        this.studyprogramme_university = studyprogramme_university;
    }
    public List<studyprogramme_CourseSlot> getStudyprogramme_courseslots() {
        return studyprogramme_courseslots;
    }

    public void addStudyprogramme_courseslot(Studyprogramme_courseslot studyprogramme_courseslot) {
        this.studyprogramme_courseslots.add(studyprogramme_courseslot);
    }

}