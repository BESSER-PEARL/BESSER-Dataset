





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Question  {

    private String type;
    private String required;
    private String description;





    private jpdl31_Question jpdl31_question;




    private jpdl31_Questionnaire jpdl31_questionnaire;


    public jpdl31_Question(
        String type,        String required,        String description    ) {
        this.type = type;
        this.required = required;
        this.description = description;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getRequired() {
        return required;
    }

    public void setRequired(String required) {
        this.required = required;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public jpdl31_Question getJpdl31_question() {
        return jpdl31_question;
    }

    public void setJpdl31_question(jpdl31_Question jpdl31_question) {
        this.jpdl31_question = jpdl31_question;
    }
    public jpdl31_Questionnaire getJpdl31_questionnaire() {
        return jpdl31_questionnaire;
    }

    public void setJpdl31_questionnaire(jpdl31_Questionnaire jpdl31_questionnaire) {
        this.jpdl31_questionnaire = jpdl31_questionnaire;
    }

}