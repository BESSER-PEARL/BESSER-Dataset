





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_Property extends MultiplicityElement, TypedElement {

    private String isComposite;
    private String default;
    private String isDerived;
    private String isReadOnly;
    private String isID;





    private Property property;




    private Class class;


    public FlatQVT_Property(
        String isComposite,        String default,        String isDerived,        String isReadOnly,        String isID    ) {
        super(
        );
        this.isComposite = isComposite;
        this.default = default;
        this.isDerived = isDerived;
        this.isReadOnly = isReadOnly;
        this.isID = isID;
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
    public String getIsid() {
        return isID;
    }

    public void setIsid(String isID) {
        this.isID = isID;
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