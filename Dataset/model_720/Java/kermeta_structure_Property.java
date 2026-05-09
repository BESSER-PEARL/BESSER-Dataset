





import java.util.List;
import java.util.ArrayList;

public class kermeta_structure_Property extends MultiplicityElement {

    private String isComposite;
    private String default;
    private String isID;
    private String isDerived;
    private String isReadOnly;
    private String isSetterAbstract;
    private String isGetterAbstract;





    private structure_Property structure_property;


    public kermeta_structure_Property(
        String isComposite,        String default,        String isID,        String isDerived,        String isReadOnly,        String isSetterAbstract,        String isGetterAbstract    ) {
        super(
        );
        this.isComposite = isComposite;
        this.default = default;
        this.isID = isID;
        this.isDerived = isDerived;
        this.isReadOnly = isReadOnly;
        this.isSetterAbstract = isSetterAbstract;
        this.isGetterAbstract = isGetterAbstract;
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
    public String getIsgetterabstract() {
        return isGetterAbstract;
    }

    public void setIsgetterabstract(String isGetterAbstract) {
        this.isGetterAbstract = isGetterAbstract;
    }

    public structure_Property getStructure_property() {
        return structure_property;
    }

    public void setStructure_property(structure_Property structure_property) {
        this.structure_property = structure_property;
    }

}