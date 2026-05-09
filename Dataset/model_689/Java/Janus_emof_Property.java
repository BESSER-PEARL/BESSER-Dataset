





import java.util.List;
import java.util.ArrayList;

public class Janus_emof_Property extends emof_TypedElement, emof_MultiplicityElement {

    private boolean isDerived;
    private boolean isComposite;
    private String default;
    private boolean isId;
    private boolean isReadOnly;





    private Class class;




    private Property property;


    public Janus_emof_Property(
        boolean isDerived,        boolean isComposite,        String default,        boolean isId,        boolean isReadOnly    ) {
        super(
        );
        this.isDerived = isDerived;
        this.isComposite = isComposite;
        this.default = default;
        this.isId = isId;
        this.isReadOnly = isReadOnly;
    }


    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }
    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public boolean getIsid() {
        return isId;
    }

    public void setIsid(boolean isId) {
        this.isId = isId;
    }
    public boolean getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(boolean isReadOnly) {
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