





import java.util.List;
import java.util.ArrayList;

public class org_structure_Property extends structure_AbstractProperty, structure_MultiplicityElement {

    private String isSetterAbstract;
    private String isComposite;
    private String isGetterAbstract;
    private String isDerived;
    private String default;
    private String isID;
    private String isReadOnly;



    public org_structure_Property(
        String isSetterAbstract,        String isComposite,        String isGetterAbstract,        String isDerived,        String default,        String isID,        String isReadOnly    ) {
        super(
        );
        this.isSetterAbstract = isSetterAbstract;
        this.isComposite = isComposite;
        this.isGetterAbstract = isGetterAbstract;
        this.isDerived = isDerived;
        this.default = default;
        this.isID = isID;
        this.isReadOnly = isReadOnly;
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
    public String getIsgetterabstract() {
        return isGetterAbstract;
    }

    public void setIsgetterabstract(String isGetterAbstract) {
        this.isGetterAbstract = isGetterAbstract;
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


}