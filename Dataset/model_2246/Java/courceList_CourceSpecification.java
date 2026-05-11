





import java.util.List;
import java.util.ArrayList;

public class courceList_CourceSpecification  {

    private int specificationYear;
    private String language;
    private float credits;
    private String name;
    private String version;
    private String semester;





    private courceList_Cource courcelist_cource;




    private courceList_EvaluationForm courcelist_evaluationform;




    private courceList_Cource courcelist_cource;




    private courceList_StudyCourceRelation courcelist_studycourcerelation;




    private courceList_Professor courcelist_professor;




    private courceList_EvaluationForm courcelist_evaluationform;


    public courceList_CourceSpecification(
        int specificationYear,        String language,        float credits,        String name,        String version,        String semester    ) {
        this.specificationYear = specificationYear;
        this.language = language;
        this.credits = credits;
        this.name = name;
        this.version = version;
        this.semester = semester;
    }


    public int getSpecificationyear() {
        return specificationYear;
    }

    public void setSpecificationyear(int specificationYear) {
        this.specificationYear = specificationYear;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getSemester() {
        return semester;
    }

    public void setSemester(String semester) {
        this.semester = semester;
    }

    public courceList_Cource getCourcelist_cource() {
        return courcelist_cource;
    }

    public void setCourcelist_cource(courceList_Cource courcelist_cource) {
        this.courcelist_cource = courcelist_cource;
    }
    public courceList_EvaluationForm getCourcelist_evaluationform() {
        return courcelist_evaluationform;
    }

    public void setCourcelist_evaluationform(courceList_EvaluationForm courcelist_evaluationform) {
        this.courcelist_evaluationform = courcelist_evaluationform;
    }
    public courceList_Cource getCourcelist_cource() {
        return courcelist_cource;
    }

    public void setCourcelist_cource(courceList_Cource courcelist_cource) {
        this.courcelist_cource = courcelist_cource;
    }
    public courceList_StudyCourceRelation getCourcelist_studycourcerelation() {
        return courcelist_studycourcerelation;
    }

    public void setCourcelist_studycourcerelation(courceList_StudyCourceRelation courcelist_studycourcerelation) {
        this.courcelist_studycourcerelation = courcelist_studycourcerelation;
    }
    public courceList_Professor getCourcelist_professor() {
        return courcelist_professor;
    }

    public void setCourcelist_professor(courceList_Professor courcelist_professor) {
        this.courcelist_professor = courcelist_professor;
    }
    public courceList_EvaluationForm getCourcelist_evaluationform() {
        return courcelist_evaluationform;
    }

    public void setCourcelist_evaluationform(courceList_EvaluationForm courcelist_evaluationform) {
        this.courcelist_evaluationform = courcelist_evaluationform;
    }

}