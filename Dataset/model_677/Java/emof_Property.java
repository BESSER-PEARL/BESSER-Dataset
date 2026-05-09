





import java.util.List;
import java.util.ArrayList;

public class emof_Property extends MultiplicityElement, TypedElement {

    private String isId;
    private String isComposite;
    private String isDerived;
    private String default;
    private String isReadOnly;





    private emof_Property emof_property;




    private emof_Class emof_class;




    private emof_Class emof_class;


    public emof_Property(
        String isId,        String isComposite,        String isDerived,        String default,        String isReadOnly    ) {
        super(
        );
        this.isId = isId;
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.default = default;
        this.isReadOnly = isReadOnly;
    }


    public String getIsid() {
        return isId;
    }

    public void setIsid(String isId) {
        this.isId = isId;
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

    public emof_Property getEmof_property() {
        return emof_property;
    }

    public void setEmof_property(emof_Property emof_property) {
        this.emof_property = emof_property;
    }
    public emof_Class getEmof_class() {
        return emof_class;
    }

    public void setEmof_class(emof_Class emof_class) {
        this.emof_class = emof_class;
    }
    public emof_Class getEmof_class() {
        return emof_class;
    }

    public void setEmof_class(emof_Class emof_class) {
        this.emof_class = emof_class;
    }

}