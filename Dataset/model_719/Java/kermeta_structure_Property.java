





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_Property extends MultiplicityElement {

    private String isComposite;
    private String isDerived;
    private String default;
    private String isGetterAbstract;
    private String isSetterAbstract;
    private String isID;
    private String isReadOnly;





    private behavior_Expression behavior_expression;




    private structure_Property structure_property;




    private behavior_Expression behavior_expression;


    public kermeta_structure_Property(
        String isComposite,        String isDerived,        String default,        String isGetterAbstract,        String isSetterAbstract,        String isID,        String isReadOnly    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.default = default;
        this.isGetterAbstract = isGetterAbstract;
        this.isSetterAbstract = isSetterAbstract;
        this.isID = isID;
        this.isReadOnly = isReadOnly;
    }


    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
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
    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }

    public behavior_Expression getBehavior_expression() {
        return behavior_expression;
    }

    public void setBehavior_expression(behavior_Expression behavior_expression) {
        this.behavior_expression = behavior_expression;
    }
    public structure_Property getStructure_property() {
        return structure_property;
    }

    public void setStructure_property(structure_Property structure_property) {
        this.structure_property = structure_property;
    }
    public behavior_Expression getBehavior_expression() {
        return behavior_expression;
    }

    public void setBehavior_expression(behavior_Expression behavior_expression) {
        this.behavior_expression = behavior_expression;
    }

}