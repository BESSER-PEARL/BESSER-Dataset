





import java.util.List;
import java.util.ArrayList;

public class aml_QuestionRelationships  {






    private aml_Question aml_question;




    private aml_DocumentRoot aml_documentroot;




    private List<aml_Dependent> aml_dependents;


    public aml_QuestionRelationships(
    ) {
        this.aml_dependents = new ArrayList<>();
    }

    public aml_QuestionRelationships(
        ArrayList<aml_Dependent> aml_dependents    ) {
        this.aml_dependents = aml_dependents;
    }


    public aml_Question getAml_question() {
        return aml_question;
    }

    public void setAml_question(aml_Question aml_question) {
        this.aml_question = aml_question;
    }
    public aml_DocumentRoot getAml_documentroot() {
        return aml_documentroot;
    }

    public void setAml_documentroot(aml_DocumentRoot aml_documentroot) {
        this.aml_documentroot = aml_documentroot;
    }
    public List<aml_Dependent> getAml_dependents() {
        return aml_dependents;
    }

    public void addAml_dependent(Aml_dependent aml_dependent) {
        this.aml_dependents.add(aml_dependent);
    }

}