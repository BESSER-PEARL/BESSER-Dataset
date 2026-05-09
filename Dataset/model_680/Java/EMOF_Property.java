





import java.util.List;
import java.util.ArrayList;

public class EMOF_Property extends TypedElement, MultiplicityElement {

    private String isComposite;
    private String default;
    private String isID;
    private String isDerived;
    private String isReadOnly;





    private Class class;


    public EMOF_Property(
        String isComposite,        String default,        String isID,        String isDerived,        String isReadOnly    ) {
        super(
        );
        this.isComposite = isComposite;
        this.default = default;
        this.isID = isID;
        this.isDerived = isDerived;
        this.isReadOnly = isReadOnly;
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

}