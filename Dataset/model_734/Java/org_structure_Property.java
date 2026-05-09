





import java.util.List;
import java.util.ArrayList;

public class org_structure_Property extends structure_MultiplicityElement, structure_AbstractProperty {

    private String default;
    private String isReadOnly;
    private String isSetterAbstract;
    private String isID;
    private String isDerived;
    private String isGetterAbstract;
    private String isComposite;





    private behavior_Expression behavior_expression;




    private behavior_Expression behavior_expression;


    public org_structure_Property(
        String default,        String isReadOnly,        String isSetterAbstract,        String isID,        String isDerived,        String isGetterAbstract,        String isComposite    ) {
        super(
        );
        this.default = default;
        this.isReadOnly = isReadOnly;
        this.isSetterAbstract = isSetterAbstract;
        this.isID = isID;
        this.isDerived = isDerived;
        this.isGetterAbstract = isGetterAbstract;
        this.isComposite = isComposite;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }
    public String getIssetterabstract() {
        return isSetterAbstract;
    }

    public void setIssetterabstract(String isSetterAbstract) {
        this.isSetterAbstract = isSetterAbstract;
    }
    public String getIsid() {
        return isID;
    }

    public void setIsid(String isID) {
        this.isID = isID;
    }
    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }
    public String getIsgetterabstract() {
        return isGetterAbstract;
    }

    public void setIsgetterabstract(String isGetterAbstract) {
        this.isGetterAbstract = isGetterAbstract;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }

    public behavior_Expression getBehavior_expression() {
        return behavior_expression;
    }

    public void setBehavior_expression(behavior_Expression behavior_expression) {
        this.behavior_expression = behavior_expression;
    }
    public behavior_Expression getBehavior_expression() {
        return behavior_expression;
    }

    public void setBehavior_expression(behavior_Expression behavior_expression) {
        this.behavior_expression = behavior_expression;
    }

}