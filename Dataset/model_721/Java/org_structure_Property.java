





import java.util.List;
import java.util.ArrayList;

public class org_structure_Property extends structure_MultiplicityElement, structure_AbstractProperty {

    private String isGetterAbstract;
    private String isID;
    private String isSetterAbstract;
    private String isComposite;
    private String isReadOnly;
    private String isDerived;
    private String default;





    private structure_ClassDefinition structure_classdefinition;




    private behavior_Expression behavior_expression;




    private behavior_Expression behavior_expression;


    public org_structure_Property(
        String isGetterAbstract,        String isID,        String isSetterAbstract,        String isComposite,        String isReadOnly,        String isDerived,        String default    ) {
        super(
        );
        this.isGetterAbstract = isGetterAbstract;
        this.isID = isID;
        this.isSetterAbstract = isSetterAbstract;
        this.isComposite = isComposite;
        this.isReadOnly = isReadOnly;
        this.isDerived = isDerived;
        this.default = default;
    }


    public String getIsgetterabstract() {
        return isGetterAbstract;
    }

    public void setIsgetterabstract(String isGetterAbstract) {
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
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
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

    public structure_ClassDefinition getStructure_classdefinition() {
        return structure_classdefinition;
    }

    public void setStructure_classdefinition(structure_ClassDefinition structure_classdefinition) {
        this.structure_classdefinition = structure_classdefinition;
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