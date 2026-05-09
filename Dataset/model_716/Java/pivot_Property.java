





import java.util.List;
import java.util.ArrayList;

public class pivot_Property extends Feature {

    private String defaultValueString;
    private String isDerived;
    private String isResolveProxies;
    private String isComposite;
    private String isID;
    private String isImplicit;
    private String isTransient;
    private String isVolatile;
    private String isReadOnly;
    private String defaultValue;
    private String isUnsettable;





    private pivot_Property pivot_property;




    private List<pivot_Property> pivot_propertys;




    private pivot_NavigationCallExp pivot_navigationcallexp;




    private List<pivot_Property> pivot_propertys;




    private pivot_Property pivot_property;




    private List<pivot_Property> pivot_propertys;


    public pivot_Property(
        String defaultValueString,        String isDerived,        String isResolveProxies,        String isComposite,        String isID,        String isImplicit,        String isTransient,        String isVolatile,        String isReadOnly,        String defaultValue,        String isUnsettable    ) {
        super(
        );
        this.defaultValueString = defaultValueString;
        this.isDerived = isDerived;
        this.isResolveProxies = isResolveProxies;
        this.isComposite = isComposite;
        this.isID = isID;
        this.isImplicit = isImplicit;
        this.isTransient = isTransient;
        this.isVolatile = isVolatile;
        this.isReadOnly = isReadOnly;
        this.defaultValue = defaultValue;
        this.isUnsettable = isUnsettable;
        this.pivot_propertys = new ArrayList<>();
        this.pivot_propertys = new ArrayList<>();
        this.pivot_propertys = new ArrayList<>();
    }

    public pivot_Property(
        String defaultValueString,        String isDerived,        String isResolveProxies,        String isComposite,        String isID,        String isImplicit,        String isTransient,        String isVolatile,        String isReadOnly,        String defaultValue,        String isUnsettable        ArrayList<pivot_Property> pivot_propertys,        ArrayList<pivot_Property> pivot_propertys,        ArrayList<pivot_Property> pivot_propertys    ) {
        this.defaultValueString = defaultValueString;
        this.isDerived = isDerived;
        this.isResolveProxies = isResolveProxies;
        this.isComposite = isComposite;
        this.isID = isID;
        this.isImplicit = isImplicit;
        this.isTransient = isTransient;
        this.isVolatile = isVolatile;
        this.isReadOnly = isReadOnly;
        this.defaultValue = defaultValue;
        this.isUnsettable = isUnsettable;
        this.pivot_propertys = pivot_propertys;
        this.pivot_propertys = pivot_propertys;
        this.pivot_propertys = pivot_propertys;
    }

    public String getDefaultvaluestring() {
        return defaultValueString;
    }

    public void setDefaultvaluestring(String defaultValueString) {
        this.defaultValueString = defaultValueString;
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
    public String getIsimplicit() {
        return isImplicit;
    }

    public void setIsimplicit(String isImplicit) {
        this.isImplicit = isImplicit;
    }
    public String getIstransient() {
        return isTransient;
    }

    public void setIstransient(String isTransient) {
        this.isTransient = isTransient;
    }
    public String getIsvolatile() {
        return isVolatile;
    }

    public void setIsvolatile(String isVolatile) {
        this.isVolatile = isVolatile;
    }
    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getIsunsettable() {
        return isUnsettable;
    }

    public void setIsunsettable(String isUnsettable) {
        this.isUnsettable = isUnsettable;
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
    public pivot_NavigationCallExp getPivot_navigationcallexp() {
        return pivot_navigationcallexp;
    }

    public void setPivot_navigationcallexp(pivot_NavigationCallExp pivot_navigationcallexp) {
        this.pivot_navigationcallexp = pivot_navigationcallexp;
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
    public List<pivot_Property> getPivot_propertys() {
        return pivot_propertys;
    }

    public void addPivot_property(Pivot_property pivot_property) {
        this.pivot_propertys.add(pivot_property);
    }

}