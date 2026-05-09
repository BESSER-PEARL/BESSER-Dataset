





import java.util.List;
import java.util.ArrayList;

public class pivot_Property extends ParameterableElement, Feature {

    private String isReadOnly;
    private String isUnsettable;
    private String isVolatile;
    private String isComposite;
    private String isDerived;
    private String isTransient;
    private String isID;
    private String implicit;
    private String default;
    private String isResolveProxies;





    private List<pivot_Property> pivot_propertys;




    private pivot_OpaqueExpression pivot_opaqueexpression;




    private pivot_PropertyCallExp pivot_propertycallexp;




    private pivot_Property pivot_property;




    private pivot_Property pivot_property;




    private List<pivot_Property> pivot_propertys;




    private pivot_Property pivot_property;


    public pivot_Property(
        String isReadOnly,        String isUnsettable,        String isVolatile,        String isComposite,        String isDerived,        String isTransient,        String isID,        String implicit,        String default,        String isResolveProxies    ) {
        super(
        );
        this.isReadOnly = isReadOnly;
        this.isUnsettable = isUnsettable;
        this.isVolatile = isVolatile;
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.isTransient = isTransient;
        this.isID = isID;
        this.implicit = implicit;
        this.default = default;
        this.isResolveProxies = isResolveProxies;
        this.pivot_propertys = new ArrayList<>();
        this.pivot_propertys = new ArrayList<>();
    }

    public pivot_Property(
        String isReadOnly,        String isUnsettable,        String isVolatile,        String isComposite,        String isDerived,        String isTransient,        String isID,        String implicit,        String default,        String isResolveProxies        ArrayList<pivot_Property> pivot_propertys,        ArrayList<pivot_Property> pivot_propertys    ) {
        this.isReadOnly = isReadOnly;
        this.isUnsettable = isUnsettable;
        this.isVolatile = isVolatile;
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.isTransient = isTransient;
        this.isID = isID;
        this.implicit = implicit;
        this.default = default;
        this.isResolveProxies = isResolveProxies;
        this.pivot_propertys = pivot_propertys;
        this.pivot_propertys = pivot_propertys;
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
    public String getIsid() {
        return isID;
    }

    public void setIsid(String isID) {
        this.isID = isID;
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
    public String getIsresolveproxies() {
        return isResolveProxies;
    }

    public void setIsresolveproxies(String isResolveProxies) {
        this.isResolveProxies = isResolveProxies;
    }

    public List<pivot_Property> getPivot_propertys() {
        return pivot_propertys;
    }

    public void addPivot_property(Pivot_property pivot_property) {
        this.pivot_propertys.add(pivot_property);
    }
    public pivot_OpaqueExpression getPivot_opaqueexpression() {
        return pivot_opaqueexpression;
    }

    public void setPivot_opaqueexpression(pivot_OpaqueExpression pivot_opaqueexpression) {
        this.pivot_opaqueexpression = pivot_opaqueexpression;
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
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }

}