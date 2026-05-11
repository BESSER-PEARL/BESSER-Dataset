





import java.util.List;
import java.util.ArrayList;

public class cmof_Property extends StructuralFeature, MultiplicityElement {

    private String default;
    private boolean isDerived;
    private boolean isComposite;
    private boolean isDerivedUnion;
    private boolean isID;
    private boolean isReadOnly;





    private cmof_Property cmof_property;




    private cmof_Property cmof_property;




    private List<cmof_Property> cmof_propertys;




    private cmof_Classifier cmof_classifier;


    public cmof_Property(
        String default,        boolean isDerived,        boolean isComposite,        boolean isDerivedUnion,        boolean isID,        boolean isReadOnly    ) {
        super(
        );
        this.default = default;
        this.isDerived = isDerived;
        this.isComposite = isComposite;
        this.isDerivedUnion = isDerivedUnion;
        this.isID = isID;
        this.isReadOnly = isReadOnly;
        this.cmof_propertys = new ArrayList<>();
    }

    public cmof_Property(
        String default,        boolean isDerived,        boolean isComposite,        boolean isDerivedUnion,        boolean isID,        boolean isReadOnly        ArrayList<cmof_Property> cmof_propertys    ) {
        this.default = default;
        this.isDerived = isDerived;
        this.isComposite = isComposite;
        this.isDerivedUnion = isDerivedUnion;
        this.isID = isID;
        this.isReadOnly = isReadOnly;
        this.cmof_propertys = cmof_propertys;
    }

    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
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
    public boolean getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(boolean isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
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

    public cmof_Property getCmof_property() {
        return cmof_property;
    }

    public void setCmof_property(cmof_Property cmof_property) {
        this.cmof_property = cmof_property;
    }
    public cmof_Property getCmof_property() {
        return cmof_property;
    }

    public void setCmof_property(cmof_Property cmof_property) {
        this.cmof_property = cmof_property;
    }
    public List<cmof_Property> getCmof_propertys() {
        return cmof_propertys;
    }

    public void addCmof_property(Cmof_property cmof_property) {
        this.cmof_propertys.add(cmof_property);
    }
    public cmof_Classifier getCmof_classifier() {
        return cmof_classifier;
    }

    public void setCmof_classifier(cmof_Classifier cmof_classifier) {
        this.cmof_classifier = cmof_classifier;
    }

}