





import java.util.List;
import java.util.ArrayList;

public class studyPlan_Specialization  {

    private String name;
    private int year;





    private List<studyPlan_SemesterProgramme> studyplan_semesterprogrammes;




    private studyPlan_StudyProgramme studyplan_studyprogramme;




    private studyPlan_SemesterProgramme studyplan_semesterprogramme;




    private List<studyPlan_Specialization> studyplan_specializations;




    private studyPlan_StudyProgramme studyplan_studyprogramme;


    public studyPlan_Specialization(
        String name,        int year    ) {
        this.name = name;
        this.year = year;
        this.studyplan_semesterprogrammes = new ArrayList<>();
        this.studyplan_specializations = new ArrayList<>();
    }

    public studyPlan_Specialization(
        String name,        int year        ArrayList<studyPlan_SemesterProgramme> studyplan_semesterprogrammes,        ArrayList<studyPlan_Specialization> studyplan_specializations    ) {
        this.name = name;
        this.year = year;
        this.studyplan_semesterprogrammes = studyplan_semesterprogrammes;
        this.studyplan_specializations = studyplan_specializations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public List<studyPlan_SemesterProgramme> getStudyplan_semesterprogrammes() {
        return studyplan_semesterprogrammes;
    }

    public void addStudyplan_semesterprogramme(Studyplan_semesterprogramme studyplan_semesterprogramme) {
        this.studyplan_semesterprogrammes.add(studyplan_semesterprogramme);
    }
    public studyPlan_StudyProgramme getStudyplan_studyprogramme() {
        return studyplan_studyprogramme;
    }

    public void setStudyplan_studyprogramme(studyPlan_StudyProgramme studyplan_studyprogramme) {
        this.studyplan_studyprogramme = studyplan_studyprogramme;
    }
    public studyPlan_SemesterProgramme getStudyplan_semesterprogramme() {
        return studyplan_semesterprogramme;
    }

    public void setStudyplan_semesterprogramme(studyPlan_SemesterProgramme studyplan_semesterprogramme) {
        this.studyplan_semesterprogramme = studyplan_semesterprogramme;
    }
    public List<studyPlan_Specialization> getStudyplan_specializations() {
        return studyplan_specializations;
    }

    public void addStudyplan_specialization(Studyplan_specialization studyplan_specialization) {
        this.studyplan_specializations.add(studyplan_specialization);
    }
    public studyPlan_StudyProgramme getStudyplan_studyprogramme() {
        return studyplan_studyprogramme;
    }

    public void setStudyplan_studyprogramme(studyPlan_StudyProgramme studyplan_studyprogramme) {
        this.studyplan_studyprogramme = studyplan_studyprogramme;
    }

}