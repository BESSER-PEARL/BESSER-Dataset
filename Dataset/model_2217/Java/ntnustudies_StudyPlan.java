





import java.util.List;
import java.util.ArrayList;

public class ntnustudies_StudyPlan  {






    private ntnustudies_Programme ntnustudies_programme;




    private List<ntnustudies_ChosenSemester> ntnustudies_chosensemesters;




    private List<ntnustudies_Specialization> ntnustudies_specializations;


    public ntnustudies_StudyPlan(
    ) {
        this.ntnustudies_chosensemesters = new ArrayList<>();
        this.ntnustudies_specializations = new ArrayList<>();
    }

    public ntnustudies_StudyPlan(
        ArrayList<ntnustudies_ChosenSemester> ntnustudies_chosensemesters,        ArrayList<ntnustudies_Specialization> ntnustudies_specializations    ) {
        this.ntnustudies_chosensemesters = ntnustudies_chosensemesters;
        this.ntnustudies_specializations = ntnustudies_specializations;
    }


    public ntnustudies_Programme getNtnustudies_programme() {
        return ntnustudies_programme;
    }

    public void setNtnustudies_programme(ntnustudies_Programme ntnustudies_programme) {
        this.ntnustudies_programme = ntnustudies_programme;
    }
    public List<ntnustudies_ChosenSemester> getNtnustudies_chosensemesters() {
        return ntnustudies_chosensemesters;
    }

    public void addNtnustudies_chosensemester(Ntnustudies_chosensemester ntnustudies_chosensemester) {
        this.ntnustudies_chosensemesters.add(ntnustudies_chosensemester);
    }
    public List<ntnustudies_Specialization> getNtnustudies_specializations() {
        return ntnustudies_specializations;
    }

    public void addNtnustudies_specialization(Ntnustudies_specialization ntnustudies_specialization) {
        this.ntnustudies_specializations.add(ntnustudies_specialization);
    }

}