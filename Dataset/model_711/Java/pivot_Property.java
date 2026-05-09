





import java.util.List;
import java.util.ArrayList;

public class pivot_Property extends Feature, ParameterableElement {

    private String implicit;
    private String default;
    private String isID;
    private String isVolatile;
    private String isComposite;
    private String isUnsettable;
    private String isReadOnly;
    private String isResolveProxies;
    private String isDerived;
    private String isTransient;





    private List<pivot_Property> pivot_propertys;




    private List<pivot_Property> pivot_propertys;




    private pivot_AssociationClass pivot_associationclass;




    private pivot_Property pivot_property;




    private pivot_Type pivot_type;




    private pivot_Property pivot_property;




    private pivot_Type pivot_type;




    private pivot_Property pivot_property;




    private pivot_Class pivot_class;




    private pivot_AssociationClass pivot_associationclass;


    public pivot_Property(
        String implicit,        String default,        String isID,        String isVolatile,        String isComposite,        String isUnsettable,        String isReadOnly,        String isResolveProxies,        String isDerived,        String isTransient    ) {
        super(
        );
        this.implicit = implicit;
        this.default = default;
        this.isID = isID;
        this.isVolatile = isVolatile;
        this.isComposite = isComposite;
        this.isUnsettable = isUnsettable;
        this.isReadOnly = isReadOnly;
        this.isResolveProxies = isResolveProxies;
        this.isDerived = isDerived;
        this.isTransient = isTransient;
        this.pivot_propertys = new ArrayList<>();
        this.pivot_propertys = new ArrayList<>();
    }

    public pivot_Property(
        String implicit,        String default,        String isID,        String isVolatile,        String isComposite,        String isUnsettable,        String isReadOnly,        String isResolveProxies,        String isDerived,        String isTransient        ArrayList<pivot_Property> pivot_propertys,        ArrayList<pivot_Property> pivot_propertys    ) {
        this.implicit = implicit;
        this.default = default;
        this.isID = isID;
        this.isVolatile = isVolatile;
        this.isComposite = isComposite;
        this.isUnsettable = isUnsettable;
        this.isReadOnly = isReadOnly;
        this.isResolveProxies = isResolveProxies;
        this.isDerived = isDerived;
        this.isTransient = isTransient;
        this.pivot_propertys = pivot_propertys;
        this.pivot_propertys = pivot_propertys;
    }

    public String getImplicit() {
        return implicit;
    }

    public void setImplicit(String implicit) {
        this.implicit = implicit;
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
    public String getIsvolatile() {
        return isVolatile;
    }

    public void setIsvolatile(String isVolatile) {
        this.isVolatile = isVolatile;
    }
    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
    }
    public String getIsunsettable() {
        return isUnsettable;
    }

    public void setIsunsettable(String isUnsettable) {
        this.isUnsettable = isUnsettable;
    }
    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
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
    public String getIstransient() {
        return isTransient;
    }

    public void setIstransient(String isTransient) {
        this.isTransient = isTransient;
    }

    public List<pivot_Property> getPivot_propertys() {
        return pivot_propertys;
    }

    public void addPivot_property(Pivot_property pivot_property) {
        this.pivot_propertys.add(pivot_property);
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
    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
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
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }
    public pivot_Class getPivot_class() {
        return pivot_class;
    }

    public void setPivot_class(pivot_Class pivot_class) {
        this.pivot_class = pivot_class;
    }
    public pivot_AssociationClass getPivot_associationclass() {
        return pivot_associationclass;
    }

    public void setPivot_associationclass(pivot_AssociationClass pivot_associationclass) {
        this.pivot_associationclass = pivot_associationclass;
    }

}