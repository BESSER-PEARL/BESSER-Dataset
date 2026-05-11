





import java.util.List;
import java.util.ArrayList;

public class cmof_Property extends StructuralFeature, MultiplicityElement {

    private boolean isReadOnly;
    private boolean isDerived;
    private String default;
    private boolean isID;
    private boolean isDerivedUnion;
    private boolean isComposite;





    private List<cmof_Property> cmof_propertys;




    private cmof_Classifier cmof_classifier;




    private cmof_Property cmof_property;




    private List<cmof_Property> cmof_propertys;


    public cmof_Property(
        boolean isReadOnly,        boolean isDerived,        String default,        boolean isID,        boolean isDerivedUnion,        boolean isComposite    ) {
        super(
        );
        this.isReadOnly = isReadOnly;
        this.isDerived = isDerived;
        this.default = default;
        this.isID = isID;
        this.isDerivedUnion = isDerivedUnion;
        this.isComposite = isComposite;
        this.cmof_propertys = new ArrayList<>();
        this.cmof_propertys = new ArrayList<>();
    }

    public cmof_Property(
        boolean isReadOnly,        boolean isDerived,        String default,        boolean isID,        boolean isDerivedUnion,        boolean isComposite        ArrayList<cmof_Property> cmof_propertys,        ArrayList<cmof_Property> cmof_propertys    ) {
        this.isReadOnly = isReadOnly;
        this.isDerived = isDerived;
        this.default = default;
        this.isID = isID;
        this.isDerivedUnion = isDerivedUnion;
        this.isComposite = isComposite;
        this.cmof_propertys = cmof_propertys;
        this.cmof_propertys = cmof_propertys;
    }

    public boolean getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(boolean isReadOnly) {
        this.isReadOnly = isReadOnly;
    }
    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public boolean getIsid() {
        return isID;
    }

    public void setIsid(boolean isID) {
        this.isID = isID;
    }
    public boolean getIsderivedunion() {
        return isDerivedUnion;
    }

    public void setIsderivedunion(boolean isDerivedUnion) {
        this.isDerivedUnion = isDerivedUnion;
    }
    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
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

}