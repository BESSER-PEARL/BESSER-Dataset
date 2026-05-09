





import java.util.List;
import java.util.ArrayList;

public class org_structure_Property extends structure_MultiplicityElement, structure_AbstractProperty {

    private String isID;
    private String isSetterAbstract;
    private String isDerived;
    private String isReadOnly;
    private String isComposite;
    private String default;
    private String isGetterAbstract;





    private behavior_Expression behavior_expression;




    private behavior_Expression behavior_expression;


    public org_structure_Property(
        String isID,        String isSetterAbstract,        String isDerived,        String isReadOnly,        String isComposite,        String default,        String isGetterAbstract    ) {
        super(
        );
        this.isID = isID;
        this.isSetterAbstract = isSetterAbstract;
        this.isDerived = isDerived;
        this.isReadOnly = isReadOnly;
        this.isComposite = isComposite;
        this.default = default;
        this.isGetterAbstract = isGetterAbstract;
    }


    public String getIsid() {
        return isID;
    }

    public void setIsid(String isID) {
        this.isID = isID;
    }
    public String getIssetterabstract() {
        return isSetterAbstract;
    }

    public void setIssetterabstract(String isSetterAbstract) {
        this.isSetterAbstract = isSetterAbstract;
    }
    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }
    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getIsgetterabstract() {
        return isGetterAbstract;
    }

    public void setIsgetterabstract(String isGetterAbstract) {
        this.isGetterAbstract = isGetterAbstract;
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