





import java.util.List;
import java.util.ArrayList;

public class EMOF_Property extends MultiplicityElement, TypedElement {

    private String isID;
    private String isDerived;
    private String default;
    private String isComposite;
    private String isReadOnly;





    private Class class;




    private Property property;


    public EMOF_Property(
        String isID,        String isDerived,        String default,        String isComposite,        String isReadOnly    ) {
        super(
        );
        this.isID = isID;
        this.isDerived = isDerived;
        this.default = default;
        this.isComposite = isComposite;
        this.isReadOnly = isReadOnly;
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
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
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

    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }
    public Property getProperty() {
        return property;
    }

    public void setProperty(Property property) {
        this.property = property;
    }

}