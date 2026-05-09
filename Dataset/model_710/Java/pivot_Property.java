





import java.util.List;
import java.util.ArrayList;

public class pivot_Property extends ParameterableElement, Feature {

    private String default;
    private String isComposite;
    private String isVolatile;
    private String isUnsettable;
    private String isID;
    private String isReadOnly;
    private String isTransient;
    private String implicit;
    private String isResolveProxies;
    private String isDerived;





    private List<pivot_Property> pivot_propertys;




    private pivot_Property pivot_property;




    private pivot_AssociationClass pivot_associationclass;




    private pivot_Property pivot_property;




    private pivot_Property pivot_property;




    private pivot_AssociationClass pivot_associationclass;




    private pivot_Property pivot_property;


    public pivot_Property(
        String default,        String isComposite,        String isVolatile,        String isUnsettable,        String isID,        String isReadOnly,        String isTransient,        String implicit,        String isResolveProxies,        String isDerived    ) {
        super(
        );
        this.default = default;
        this.isComposite = isComposite;
        this.isVolatile = isVolatile;
        this.isUnsettable = isUnsettable;
        this.isID = isID;
        this.isReadOnly = isReadOnly;
        this.isTransient = isTransient;
        this.implicit = implicit;
        this.isResolveProxies = isResolveProxies;
        this.isDerived = isDerived;
        this.pivot_propertys = new ArrayList<>();
    }

    public pivot_Property(
        String default,        String isComposite,        String isVolatile,        String isUnsettable,        String isID,        String isReadOnly,        String isTransient,        String implicit,        String isResolveProxies,        String isDerived        ArrayList<pivot_Property> pivot_propertys    ) {
        this.default = default;
        this.isComposite = isComposite;
        this.isVolatile = isVolatile;
        this.isUnsettable = isUnsettable;
        this.isID = isID;
        this.isReadOnly = isReadOnly;
        this.isTransient = isTransient;
        this.implicit = implicit;
        this.isResolveProxies = isResolveProxies;
        this.isDerived = isDerived;
        this.pivot_propertys = pivot_propertys;
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
    public String getIsvolatile() {
        return isVolatile;
    }

    public void setIsvolatile(String isVolatile) {
        this.isVolatile = isVolatile;
    }
    public String getIsunsettable() {
        return isUnsettable;
    }

    public void setIsunsettable(String isUnsettable) {
        this.isUnsettable = isUnsettable;
    }
    public String getIsid() {
        return isID;
    }

    public void setIsid(String isID) {
        this.isID = isID;
    }
    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }
    public String getIstransient() {
        return isTransient;
    }

    public void setIstransient(String isTransient) {
        this.isTransient = isTransient;
    }
    public String getImplicit() {
        return implicit;
    }

    public void setImplicit(String implicit) {
        this.implicit = implicit;
    }
    public String getIsresolveproxies() {
        return isResolveProxies;
    }

    public void setIsresolveproxies(String isResolveProxies) {
        this.isResolveProxies = isResolveProxies;
    }
    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }

    public List<pivot_Property> getPivot_propertys() {
        return pivot_propertys;
    }

    public void addPivot_property(Pivot_property pivot_property) {
        this.pivot_propertys.add(pivot_property);
    }
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
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

}