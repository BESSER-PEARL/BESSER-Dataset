





import java.util.List;
import java.util.ArrayList;

public class Janus_emof_Property extends emof_TypedElement, emof_MultiplicityElement {

    private boolean isComposite;
    private boolean isReadOnly;
    private String default;
    private boolean isId;
    private boolean isDerived;





    private Property property;




    private Class class;


    public Janus_emof_Property(
        boolean isComposite,        boolean isReadOnly,        String default,        boolean isId,        boolean isDerived    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isReadOnly = isReadOnly;
        this.default = default;
        this.isId = isId;
        this.isDerived = isDerived;
    }


    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public boolean getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(boolean isReadOnly) {
        this.isReadOnly = isReadOnly;
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
    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
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