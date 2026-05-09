





import java.util.List;
import java.util.ArrayList;

public class OCL_Property extends MultiplicityElement, TypedElement {

    private String default;
    private String isComposite;
    private String isDerived;
    private String isId;
    private String isReadOnly;





    private Property property;


    public OCL_Property(
        String default,        String isComposite,        String isDerived,        String isId,        String isReadOnly    ) {
        super(
        );
        this.default = default;
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.isId = isId;
        this.isReadOnly = isReadOnly;
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
    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }
    public String getIsid() {
        return isId;
    }

    public void setIsid(String isId) {
        this.isId = isId;
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

}