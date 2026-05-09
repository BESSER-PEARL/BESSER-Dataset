





import java.util.List;
import java.util.ArrayList;

public class EMOF_Property extends MultiplicityElement, TypedElement {

    private String isDerived;
    private String isComposite;
    private String isID;
    private String default;
    private String isReadOnly;





    private Property property;




    private Class class;


    public EMOF_Property(
        String isDerived,        String isComposite,        String isID,        String default,        String isReadOnly    ) {
        super(
        );
        this.isDerived = isDerived;
        this.isComposite = isComposite;
        this.isID = isID;
        this.default = default;
        this.isReadOnly = isReadOnly;
    }


    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getIsid() {
        return isID;
    }

    public void setIsid(String isID) {
        this.isID = isID;
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

    public Property getProperty() {
        return property;
    }

    public void setProperty(Property property) {
        this.property = property;
    }
    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }

}