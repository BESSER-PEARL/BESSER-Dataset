





import java.util.List;
import java.util.ArrayList;

public class emof_Property extends TypedElement, MultiplicityElement {

    private String isId;
    private String isReadOnly;
    private String isDerived;
    private String isComposite;
    private String default;





    private Class class;




    private Property property;


    public emof_Property(
        String isId,        String isReadOnly,        String isDerived,        String isComposite,        String default    ) {
        super(
        );
        this.isId = isId;
        this.isReadOnly = isReadOnly;
        this.isDerived = isDerived;
        this.isComposite = isComposite;
        this.default = default;
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
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
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