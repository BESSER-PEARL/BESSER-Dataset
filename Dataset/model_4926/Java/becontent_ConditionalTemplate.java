





import java.util.List;
import java.util.ArrayList;

public class becontent_ConditionalTemplate  {

    private String conditionExp;
    private String trueTemplate;
    private String fieldName;
    private String falseTemplate;
    private String _id_model;





    private becontent_Content becontent_content;


    public becontent_ConditionalTemplate(
        String conditionExp,        String trueTemplate,        String fieldName,        String falseTemplate,        String _id_model    ) {
        this.conditionExp = conditionExp;
        this.trueTemplate = trueTemplate;
        this.fieldName = fieldName;
        this.falseTemplate = falseTemplate;
        this._id_model = _id_model;
    }


    public String getConditionexp() {
        return conditionExp;
    }

    public void setConditionexp(String conditionExp) {
        this.conditionExp = conditionExp;
    }
    public String getTruetemplate() {
        return trueTemplate;
    }

    public void setTruetemplate(String trueTemplate) {
        this.trueTemplate = trueTemplate;
    }
    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }
    public String getFalsetemplate() {
        return falseTemplate;
    }

    public void setFalsetemplate(String falseTemplate) {
        this.falseTemplate = falseTemplate;
    }
    public String get_id_model() {
        return _id_model;
    }

    public void set_id_model(String _id_model) {
        this._id_model = _id_model;
    }

    public becontent_Content getBecontent_content() {
        return becontent_content;
    }

    public void setBecontent_content(becontent_Content becontent_content) {
        this.becontent_content = becontent_content;
    }

}