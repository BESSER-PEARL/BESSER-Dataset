





import java.util.List;
import java.util.ArrayList;

public class studyprogramme_Specialization extends SemesterContainer {

    private String name;
    private int selectionSemester;





    private studyprogramme_Specialization studyprogramme_specialization;




    private studyprogramme_Programme studyprogramme_programme;




    private studyprogramme_Programme studyprogramme_programme;




    private List<studyprogramme_Specialization> studyprogramme_specializations;


    public studyprogramme_Specialization(
        String name,        int selectionSemester    ) {
        super(
        );
        this.name = name;
        this.selectionSemester = selectionSemester;
        this.studyprogramme_specializations = new ArrayList<>();
    }

    public studyprogramme_Specialization(
        String name,        int selectionSemester        ArrayList<studyprogramme_Specialization> studyprogramme_specializations    ) {
        this.name = name;
        this.selectionSemester = selectionSemester;
        this.studyprogramme_specializations = studyprogramme_specializations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getSelectionsemester() {
        return selectionSemester;
    }

    public void setSelectionsemester(int selectionSemester) {
        this.selectionSemester = selectionSemester;
    }

    public studyprogramme_Specialization getStudyprogramme_specialization() {
        return studyprogramme_specialization;
    }

    public void setStudyprogramme_specialization(studyprogramme_Specialization studyprogramme_specialization) {
        this.studyprogramme_specialization = studyprogramme_specialization;
    }
    public studyprogramme_Programme getStudyprogramme_programme() {
        return studyprogramme_programme;
    }

    public void setStudyprogramme_programme(studyprogramme_Programme studyprogramme_programme) {
        this.studyprogramme_programme = studyprogramme_programme;
    }
    public studyprogramme_Programme getStudyprogramme_programme() {
        return studyprogramme_programme;
    }

    public void setStudyprogramme_programme(studyprogramme_Programme studyprogramme_programme) {
        this.studyprogramme_programme = studyprogramme_programme;
    }
    public List<studyprogramme_Specialization> getStudyprogramme_specializations() {
        return studyprogramme_specializations;
    }

    public void addStudyprogramme_specialization(Studyprogramme_specialization studyprogramme_specialization) {
        this.studyprogramme_specializations.add(studyprogramme_specialization);
    }

}