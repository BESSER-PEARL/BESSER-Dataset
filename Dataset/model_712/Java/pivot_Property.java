





import java.util.List;
import java.util.ArrayList;

public class pivot_Property extends ParameterableElement, Feature {

    private String default;
    private String isUnsettable;
    private String implicit;
    private String isVolatile;
    private String isID;
    private String isDerived;
    private String isResolveProxies;
    private String isTransient;
    private String isReadOnly;
    private String isComposite;





    private List<pivot_Property> pivot_propertys;




    private pivot_AssociationClass pivot_associationclass;




    private pivot_Property pivot_property;




    private List<pivot_Property> pivot_propertys;




    private pivot_AssociationClass pivot_associationclass;




    private pivot_Property pivot_property;




    private pivot_Property pivot_property;




    private pivot_Type pivot_type;




    private pivot_Type pivot_type;


    public pivot_Property(
        String default,        String isUnsettable,        String implicit,        String isVolatile,        String isID,        String isDerived,        String isResolveProxies,        String isTransient,        String isReadOnly,        String isComposite    ) {
        super(
        );
        this.default = default;
        this.isUnsettable = isUnsettable;
        this.implicit = implicit;
        this.isVolatile = isVolatile;
        this.isID = isID;
        this.isDerived = isDerived;
        this.isResolveProxies = isResolveProxies;
        this.isTransient = isTransient;
        this.isReadOnly = isReadOnly;
        this.isComposite = isComposite;
        this.pivot_propertys = new ArrayList<>();
        this.pivot_propertys = new ArrayList<>();
    }

    public pivot_Property(
        String default,        String isUnsettable,        String implicit,        String isVolatile,        String isID,        String isDerived,        String isResolveProxies,        String isTransient,        String isReadOnly,        String isComposite        ArrayList<pivot_Property> pivot_propertys,        ArrayList<pivot_Property> pivot_propertys    ) {
        this.default = default;
        this.isUnsettable = isUnsettable;
        this.implicit = implicit;
        this.isVolatile = isVolatile;
        this.isID = isID;
        this.isDerived = isDerived;
        this.isResolveProxies = isResolveProxies;
        this.isTransient = isTransient;
        this.isReadOnly = isReadOnly;
        this.isComposite = isComposite;
        this.pivot_propertys = pivot_propertys;
        this.pivot_propertys = pivot_propertys;
    }

    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getIsunsettable() {
        return isUnsettable;
    }

    public void setIsunsettable(String isUnsettable) {
        this.isUnsettable = isUnsettable;
    }
    public String getImplicit() {
        return implicit;
    }

    public void setImplicit(String implicit) {
        this.implicit = implicit;
    }
    public String getIsvolatile() {
        return isVolatile;
    }

    public void setIsvolatile(String isVolatile) {
        this.isVolatile = isVolatile;
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
    public String getIsresolveproxies() {
        return isResolveProxies;
    }

    public void setIsresolveproxies(String isResolveProxies) {
        this.isResolveProxies = isResolveProxies;
    }
    public String getIstransient() {
        return isTransient;
    }

    public void setIstransient(String isTransient) {
        this.isTransient = isTransient;
    }
    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }

    public List<pivot_Property> getPivot_propertys() {
        return pivot_propertys;
    }

    public void addPivot_property(Pivot_property pivot_property) {
        this.pivot_propertys.add(pivot_property);
    }
    public pivot_AssociationClass getPivot_associationclass() {
        return pivot_associationclass;
    }

    public void setPivot_associationclass(pivot_AssociationClass pivot_associationclass) {
        this.pivot_associationclass = pivot_associationclass;
    }
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }
    public List<pivot_Property> getPivot_propertys() {
        return pivot_propertys;
    }

    public void addPivot_property(Pivot_property pivot_property) {
        this.pivot_propertys.add(pivot_property);
    }
    public pivot_AssociationClass getPivot_associationclass() {
        return pivot_associationclass;
    }

    public void setPivot_associationclass(pivot_AssociationClass pivot_associationclass) {
        this.pivot_associationclass = pivot_associationclass;
    }
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }
    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }
    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }

}