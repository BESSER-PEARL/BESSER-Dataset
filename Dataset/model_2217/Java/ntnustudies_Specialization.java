





import java.util.List;
import java.util.ArrayList;

public class ntnustudies_Specialization  {

    private int specializationChoicePointSemester;
    private String name;





    private ntnustudies_Programme ntnustudies_programme;




    private List<ntnustudies_Course> ntnustudies_courses;




    private ntnustudies_Programme ntnustudies_programme;




    private ntnustudies_Specialization ntnustudies_specialization;


    public ntnustudies_Specialization(
        int specializationChoicePointSemester,        String name    ) {
        this.specializationChoicePointSemester = specializationChoicePointSemester;
        this.name = name;
        this.ntnustudies_courses = new ArrayList<>();
    }

    public ntnustudies_Specialization(
        int specializationChoicePointSemester,        String name        ArrayList<ntnustudies_Course> ntnustudies_courses    ) {
        this.specializationChoicePointSemester = specializationChoicePointSemester;
        this.name = name;
        this.ntnustudies_courses = ntnustudies_courses;
    }

    public int getSpecializationchoicepointsemester() {
        return specializationChoicePointSemester;
    }

    public void setSpecializationchoicepointsemester(int specializationChoicePointSemester) {
        this.specializationChoicePointSemester = specializationChoicePointSemester;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ntnustudies_Programme getNtnustudies_programme() {
        return ntnustudies_programme;
    }

    public void setNtnustudies_programme(ntnustudies_Programme ntnustudies_programme) {
        this.ntnustudies_programme = ntnustudies_programme;
    }
    public List<ntnustudies_Course> getNtnustudies_courses() {
        return ntnustudies_courses;
    }

    public void addNtnustudies_course(Ntnustudies_course ntnustudies_course) {
        this.ntnustudies_courses.add(ntnustudies_course);
    }
    public ntnustudies_Programme getNtnustudies_programme() {
        return ntnustudies_programme;
    }

    public void setNtnustudies_programme(ntnustudies_Programme ntnustudies_programme) {
        this.ntnustudies_programme = ntnustudies_programme;
    }
    public ntnustudies_Specialization getNtnustudies_specialization() {
        return ntnustudies_specialization;
    }

    public void setNtnustudies_specialization(ntnustudies_Specialization ntnustudies_specialization) {
        this.ntnustudies_specialization = ntnustudies_specialization;
    }

}