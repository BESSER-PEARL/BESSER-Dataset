





import java.util.List;
import java.util.ArrayList;

public class SecCon_Attribute extends MultiplicityElement, TypedElement {

    private boolean isComposite;
    private boolean isDerived;
    private boolean isID;
    private boolean isReadOnly;
    private String default;





    private SecCon_Attribute seccon_attribute;




    private SecCon_Class seccon_class;


    public SecCon_Attribute(
        boolean isComposite,        boolean isDerived,        boolean isID,        boolean isReadOnly,        String default    ) {
        super(
        );
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.isID = isID;
        this.isReadOnly = isReadOnly;
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
    public boolean getIsid() {
        return isID;
    }

    public void setIsid(boolean isID) {
        this.isID = isID;
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

    public SecCon_Attribute getSeccon_attribute() {
        return seccon_attribute;
    }

    public void setSeccon_attribute(SecCon_Attribute seccon_attribute) {
        this.seccon_attribute = seccon_attribute;
    }
    public SecCon_Class getSeccon_class() {
        return seccon_class;
    }

    public void setSeccon_class(SecCon_Class seccon_class) {
        this.seccon_class = seccon_class;
    }

}