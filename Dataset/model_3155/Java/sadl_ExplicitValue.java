





import java.util.List;
import java.util.ArrayList;

public class sadl_ExplicitValue  {

    private String term;
    private String valueList;





    private sadl_HasValueCondition sadl_hasvaluecondition;




    private sadl_ResourceByName sadl_resourcebyname;




    private sadl_DefaultValue sadl_defaultvalue;




    private sadl_LiteralValue sadl_literalvalue;


    public sadl_ExplicitValue(
        String term,        String valueList    ) {
        this.term = term;
        this.valueList = valueList;
    }


    public String getTerm() {
        return term;
    }

    public void setTerm(String term) {
        this.term = term;
    }
    public String getValuelist() {
        return valueList;
    }

    public void setValuelist(String valueList) {
        this.valueList = valueList;
    }

    public sadl_HasValueCondition getSadl_hasvaluecondition() {
        return sadl_hasvaluecondition;
    }

    public void setSadl_hasvaluecondition(sadl_HasValueCondition sadl_hasvaluecondition) {
        this.sadl_hasvaluecondition = sadl_hasvaluecondition;
    }
    public sadl_ResourceByName getSadl_resourcebyname() {
        return sadl_resourcebyname;
    }

    public void setSadl_resourcebyname(sadl_ResourceByName sadl_resourcebyname) {
        this.sadl_resourcebyname = sadl_resourcebyname;
    }
    public sadl_DefaultValue getSadl_defaultvalue() {
        return sadl_defaultvalue;
    }

    public void setSadl_defaultvalue(sadl_DefaultValue sadl_defaultvalue) {
        this.sadl_defaultvalue = sadl_defaultvalue;
    }
    public sadl_LiteralValue getSadl_literalvalue() {
        return sadl_literalvalue;
    }

    public void setSadl_literalvalue(sadl_LiteralValue sadl_literalvalue) {
        this.sadl_literalvalue = sadl_literalvalue;
    }

}