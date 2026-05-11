





import java.util.List;
import java.util.ArrayList;

public class universityStudies_Semester  {

    private String name;
    private String season;
    private int semesterNumber;





    private universityStudies_Programme universitystudies_programme;




    private List<universityStudies_CourseSlot> universitystudies_courseslots;




    private universityStudies_Specialization universitystudies_specialization;


    public universityStudies_Semester(
        String name,        String season,        int semesterNumber    ) {
        this.name = name;
        this.season = season;
        this.semesterNumber = semesterNumber;
        this.universitystudies_courseslots = new ArrayList<>();
    }

    public universityStudies_Semester(
        String name,        String season,        int semesterNumber        ArrayList<universityStudies_CourseSlot> universitystudies_courseslots    ) {
        this.name = name;
        this.season = season;
        this.semesterNumber = semesterNumber;
        this.universitystudies_courseslots = universitystudies_courseslots;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSeason() {
        return season;
    }

    public void setSeason(String season) {
        this.season = season;
    }
    public int getSemesternumber() {
        return semesterNumber;
    }

    public void setSemesternumber(int semesterNumber) {
        this.semesterNumber = semesterNumber;
    }

    public universityStudies_Programme getUniversitystudies_programme() {
        return universitystudies_programme;
    }

    public void setUniversitystudies_programme(universityStudies_Programme universitystudies_programme) {
        this.universitystudies_programme = universitystudies_programme;
    }
    public List<universityStudies_CourseSlot> getUniversitystudies_courseslots() {
        return universitystudies_courseslots;
    }

    public void addUniversitystudies_courseslot(Universitystudies_courseslot universitystudies_courseslot) {
        this.universitystudies_courseslots.add(universitystudies_courseslot);
    }
    public universityStudies_Specialization getUniversitystudies_specialization() {
        return universitystudies_specialization;
    }

    public void setUniversitystudies_specialization(universityStudies_Specialization universitystudies_specialization) {
        this.universitystudies_specialization = universitystudies_specialization;
    }

}