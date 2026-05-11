





import java.util.List;
import java.util.ArrayList;

public class universityStudies_Department  {






    private universityStudies_Programme universitystudies_programme;




    private List<universityStudies_Course> universitystudies_courses;




    private universityStudies_Programme universitystudies_programme;


    public universityStudies_Department(
    ) {
        this.universitystudies_courses = new ArrayList<>();
    }

    public universityStudies_Department(
        ArrayList<universityStudies_Course> universitystudies_courses    ) {
        this.universitystudies_courses = universitystudies_courses;
    }


    public universityStudies_Programme getUniversitystudies_programme() {
        return universitystudies_programme;
    }

    public void setUniversitystudies_programme(universityStudies_Programme universitystudies_programme) {
        this.universitystudies_programme = universitystudies_programme;
    }
    public List<universityStudies_Course> getUniversitystudies_courses() {
        return universitystudies_courses;
    }

    public void addUniversitystudies_course(Universitystudies_course universitystudies_course) {
        this.universitystudies_courses.add(universitystudies_course);
    }
    public universityStudies_Programme getUniversitystudies_programme() {
        return universitystudies_programme;
    }

    public void setUniversitystudies_programme(universityStudies_Programme universitystudies_programme) {
        this.universitystudies_programme = universitystudies_programme;
    }

}