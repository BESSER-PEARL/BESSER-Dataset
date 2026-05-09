





import java.util.List;
import java.util.ArrayList;

public class JTLMM_emof_Property extends emof_MultiplicityElement, emof_TypedElement {

    private boolean isComposite;
    private boolean isDerived;
    private boolean isReadOnly;
    private boolean isId;
    private String default;





    private Class class;




    private Property property;


    public JTLMM_emof_Property(
        boolean isComposite,        boolean isDerived,        boolean isReadOnly,        boolean isId,        String default    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.isReadOnly = isReadOnly;
        this.isId = isId;
        this.default = default;
    }


    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }
    public boolean getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(boolean isReadOnly) {
        this.isReadOnly = isReadOnly;
    }
    public boolean getIsid() {
        return isId;
    }

    public void setIsid(boolean isId) {
        this.isId = isId;
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