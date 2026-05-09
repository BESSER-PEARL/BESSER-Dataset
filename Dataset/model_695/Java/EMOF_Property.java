





import java.util.List;
import java.util.ArrayList;

public class EMOF_Property extends MultiplicityElement, TypedElement {

    private String isReadOnly;
    private String default;
    private String isID;
    private String isDerived;
    private String isComposite;





    private Property property;




    private Class class;


    public EMOF_Property(
        String isReadOnly,        String default,        String isID,        String isDerived,        String isComposite    ) {
        super(
        );
        this.isReadOnly = isReadOnly;
        this.default = default;
        this.isID = isID;
        this.isDerived = isDerived;
        this.isComposite = isComposite;
    }


    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
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
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
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