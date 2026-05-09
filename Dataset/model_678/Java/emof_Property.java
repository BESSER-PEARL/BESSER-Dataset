





import java.util.List;
import java.util.ArrayList;

public class emof_Property extends TypedElement, MultiplicityElement {

    private String isId;
    private String default;
    private String isReadOnly;
    private String isDerived;
    private String isComposite;





    private emof_Class emof_class;




    private emof_Property emof_property;




    private emof_Class emof_class;


    public emof_Property(
        String isId,        String default,        String isReadOnly,        String isDerived,        String isComposite    ) {
        super(
        );
        this.isId = isId;
        this.default = default;
        this.isReadOnly = isReadOnly;
        this.isDerived = isDerived;
        this.isComposite = isComposite;
    }


    public String getIsid() {
        return isId;
    }

    public void setIsid(String isId) {
        this.isId = isId;
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

    public emof_Class getEmof_class() {
        return emof_class;
    }

    public void setEmof_class(emof_Class emof_class) {
        this.emof_class = emof_class;
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

}