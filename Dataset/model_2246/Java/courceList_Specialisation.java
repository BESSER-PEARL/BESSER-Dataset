





import java.util.List;
import java.util.ArrayList;

public class courceList_Specialisation  {

    private String name;
    private int startSemester;





    private courceList_Specialisation courcelist_specialisation;




    private courceList_StudyCourceRelation courcelist_studycourcerelation;




    private List<courceList_StudyCourceRelation> courcelist_studycourcerelations;




    private courceList_StudyProgram courcelist_studyprogram;




    private List<courceList_Specialisation> courcelist_specialisations;




    private courceList_StudyProgram courcelist_studyprogram;


    public courceList_Specialisation(
        String name,        int startSemester    ) {
        this.name = name;
        this.startSemester = startSemester;
        this.courcelist_studycourcerelations = new ArrayList<>();
        this.courcelist_specialisations = new ArrayList<>();
    }

    public courceList_Specialisation(
        String name,        int startSemester        ArrayList<courceList_StudyCourceRelation> courcelist_studycourcerelations,        ArrayList<courceList_Specialisation> courcelist_specialisations    ) {
        this.name = name;
        this.startSemester = startSemester;
        this.courcelist_studycourcerelations = courcelist_studycourcerelations;
        this.courcelist_specialisations = courcelist_specialisations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getStartsemester() {
        return startSemester;
    }

    public void setStartsemester(int startSemester) {
        this.startSemester = startSemester;
    }

    public courceList_Specialisation getCourcelist_specialisation() {
        return courcelist_specialisation;
    }

    public void setCourcelist_specialisation(courceList_Specialisation courcelist_specialisation) {
        this.courcelist_specialisation = courcelist_specialisation;
    }
    public courceList_StudyCourceRelation getCourcelist_studycourcerelation() {
        return courcelist_studycourcerelation;
    }

    public void setCourcelist_studycourcerelation(courceList_StudyCourceRelation courcelist_studycourcerelation) {
        this.courcelist_studycourcerelation = courcelist_studycourcerelation;
    }
    public List<courceList_StudyCourceRelation> getCourcelist_studycourcerelations() {
        return courcelist_studycourcerelations;
    }

    public void addCourcelist_studycourcerelation(Courcelist_studycourcerelation courcelist_studycourcerelation) {
        this.courcelist_studycourcerelations.add(courcelist_studycourcerelation);
    }
    public courceList_StudyProgram getCourcelist_studyprogram() {
        return courcelist_studyprogram;
    }

    public void setCourcelist_studyprogram(courceList_StudyProgram courcelist_studyprogram) {
        this.courcelist_studyprogram = courcelist_studyprogram;
    }
    public List<courceList_Specialisation> getCourcelist_specialisations() {
        return courcelist_specialisations;
    }

    public void addCourcelist_specialisation(Courcelist_specialisation courcelist_specialisation) {
        this.courcelist_specialisations.add(courcelist_specialisation);
    }
    public courceList_StudyProgram getCourcelist_studyprogram() {
        return courcelist_studyprogram;
    }

    public void setCourcelist_studyprogram(courceList_StudyProgram courcelist_studyprogram) {
        this.courcelist_studyprogram = courcelist_studyprogram;
    }

}