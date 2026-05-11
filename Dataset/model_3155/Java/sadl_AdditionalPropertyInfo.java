





import java.util.List;
import java.util.ArrayList;

public class sadl_AdditionalPropertyInfo  {

    private String isinvfunc;
    private String isfunc;
    private String isSym;
    private String isTrans;





    private sadl_Range sadl_range;




    private sadl_PropertyDeclaration sadl_propertydeclaration;




    private sadl_ResourceIdentifier sadl_resourceidentifier;




    private sadl_Condition sadl_condition;


    public sadl_AdditionalPropertyInfo(
        String isinvfunc,        String isfunc,        String isSym,        String isTrans    ) {
        this.isinvfunc = isinvfunc;
        this.isfunc = isfunc;
        this.isSym = isSym;
        this.isTrans = isTrans;
    }


    public String getIsinvfunc() {
        return isinvfunc;
    }

    public void setIsinvfunc(String isinvfunc) {
        this.isinvfunc = isinvfunc;
    }
    public String getIsfunc() {
        return isfunc;
    }

    public void setIsfunc(String isfunc) {
        this.isfunc = isfunc;
    }
    public String getIssym() {
        return isSym;
    }

    public void setIssym(String isSym) {
        this.isSym = isSym;
    }
    public String getIstrans() {
        return isTrans;
    }

    public void setIstrans(String isTrans) {
        this.isTrans = isTrans;
    }

    public sadl_Range getSadl_range() {
        return sadl_range;
    }

    public void setSadl_range(sadl_Range sadl_range) {
        this.sadl_range = sadl_range;
    }
    public sadl_PropertyDeclaration getSadl_propertydeclaration() {
        return sadl_propertydeclaration;
    }

    public void setSadl_propertydeclaration(sadl_PropertyDeclaration sadl_propertydeclaration) {
        this.sadl_propertydeclaration = sadl_propertydeclaration;
    }
    public sadl_ResourceIdentifier getSadl_resourceidentifier() {
        return sadl_resourceidentifier;
    }

    public void setSadl_resourceidentifier(sadl_ResourceIdentifier sadl_resourceidentifier) {
        this.sadl_resourceidentifier = sadl_resourceidentifier;
    }
    public sadl_Condition getSadl_condition() {
        return sadl_condition;
    }

    public void setSadl_condition(sadl_Condition sadl_condition) {
        this.sadl_condition = sadl_condition;
    }

}