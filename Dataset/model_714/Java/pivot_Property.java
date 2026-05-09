





import java.util.List;
import java.util.ArrayList;

public class pivot_Property extends ParameterableElement, Feature {

    private String isComposite;
    private String implicit;
    private String isResolveProxies;
    private String isReadOnly;
    private String isUnsettable;
    private String isDerived;
    private String isTransient;
    private String default;
    private String isID;
    private String isVolatile;





    private pivot_Class pivot_class;




    private pivot_Property pivot_property;




    private pivot_Type pivot_type;




    private pivot_Property pivot_property;




    private pivot_Property pivot_property;




    private pivot_Type pivot_type;




    private pivot_AssociationClass pivot_associationclass;




    private pivot_AssociationClass pivot_associationclass;




    private pivot_PropertyCallExp pivot_propertycallexp;




    private pivot_Property pivot_property;




    private List<pivot_Property> pivot_propertys;


    public pivot_Property(
        String isComposite,        String implicit,        String isResolveProxies,        String isReadOnly,        String isUnsettable,        String isDerived,        String isTransient,        String default,        String isID,        String isVolatile    ) {
        super(
        );
        this.isComposite = isComposite;
        this.implicit = implicit;
        this.isResolveProxies = isResolveProxies;
        this.isReadOnly = isReadOnly;
        this.isUnsettable = isUnsettable;
        this.isDerived = isDerived;
        this.isTransient = isTransient;
        this.default = default;
        this.isID = isID;
        this.isVolatile = isVolatile;
        this.pivot_propertys = new ArrayList<>();
    }

    public pivot_Property(
        String isComposite,        String implicit,        String isResolveProxies,        String isReadOnly,        String isUnsettable,        String isDerived,        String isTransient,        String default,        String isID,        String isVolatile        ArrayList<pivot_Property> pivot_propertys    ) {
        this.isComposite = isComposite;
        this.implicit = implicit;
        this.isResolveProxies = isResolveProxies;
        this.isReadOnly = isReadOnly;
        this.isUnsettable = isUnsettable;
        this.isDerived = isDerived;
        this.isTransient = isTransient;
        this.default = default;
        this.isID = isID;
        this.isVolatile = isVolatile;
        this.pivot_propertys = pivot_propertys;
    }

    public String getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(String isComposite) {
        this.isComposite = isComposite;
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
    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }
    public String getIsunsettable() {
        return isUnsettable;
    }

    public void setIsunsettable(String isUnsettable) {
        this.isUnsettable = isUnsettable;
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

    public pivot_Class getPivot_class() {
        return pivot_class;
    }

    public void setPivot_class(pivot_Class pivot_class) {
        this.pivot_class = pivot_class;
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
    public pivot_AssociationClass getPivot_associationclass() {
        return pivot_associationclass;
    }

    public void setPivot_associationclass(pivot_AssociationClass pivot_associationclass) {
        this.pivot_associationclass = pivot_associationclass;
    }
    public pivot_AssociationClass getPivot_associationclass() {
        return pivot_associationclass;
    }

    public void setPivot_associationclass(pivot_AssociationClass pivot_associationclass) {
        this.pivot_associationclass = pivot_associationclass;
    }
    public pivot_PropertyCallExp getPivot_propertycallexp() {
        return pivot_propertycallexp;
    }

    public void setPivot_propertycallexp(pivot_PropertyCallExp pivot_propertycallexp) {
        this.pivot_propertycallexp = pivot_propertycallexp;
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

}