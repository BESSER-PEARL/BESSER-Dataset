





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_Property extends TypedElement, MultiplicityElement {

    private String isReadOnly;
    private String isDerived;
    private String default;
    private String isComposite;
    private String isID;



    public FlatQVT_Property(
        String isReadOnly,        String isDerived,        String default,        String isComposite,        String isID    ) {
        super(
        );
        this.isReadOnly = isReadOnly;
        this.isDerived = isDerived;
        this.default = default;
        this.isComposite = isComposite;
        this.isID = isID;
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
    public String getIsid() {
        return isID;
    }

    public void setIsid(String isID) {
        this.isID = isID;
    }


}