





import java.util.List;
import java.util.ArrayList;

public class aml_EvidenceExhibit  {

    private String questionId;
    private String value;
    private String idRef;





    private aml_Evidence aml_evidence;




    private aml_DocumentRoot aml_documentroot;


    public aml_EvidenceExhibit(
        String questionId,        String value,        String idRef    ) {
        this.questionId = questionId;
        this.value = value;
        this.idRef = idRef;
    }


    public String getQuestionid() {
        return questionId;
    }

    public void setQuestionid(String questionId) {
        this.questionId = questionId;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getIdref() {
        return idRef;
    }

    public void setIdref(String idRef) {
        this.idRef = idRef;
    }

    public aml_Evidence getAml_evidence() {
        return aml_evidence;
    }

    public void setAml_evidence(aml_Evidence aml_evidence) {
        this.aml_evidence = aml_evidence;
    }
    public aml_DocumentRoot getAml_documentroot() {
        return aml_documentroot;
    }

    public void setAml_documentroot(aml_DocumentRoot aml_documentroot) {
        this.aml_documentroot = aml_documentroot;
    }

}