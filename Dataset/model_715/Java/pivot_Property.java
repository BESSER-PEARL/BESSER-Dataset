





import java.util.List;
import java.util.ArrayList;

public class pivot_Property extends Feature {

    private String isID;
    private String isReadOnly;
    private String isTransient;
    private String isImplicit;
    private String isUnsettable;
    private String isResolveProxies;
    private String isDerived;
    private String defaultValueString;
    private String defaultValue;
    private String isComposite;
    private String isVolatile;





    private pivot_AssociationClass pivot_associationclass;




    private pivot_Class pivot_class;




    private pivot_AssociationClass pivot_associationclass;




    private pivot_Class pivot_class;




    private List<pivot_Property> pivot_propertys;




    private pivot_Property pivot_property;




    private pivot_Property pivot_property;




    private pivot_Property pivot_property;




    private pivot_Property pivot_property;


    public pivot_Property(
        String isID,        String isReadOnly,        String isTransient,        String isImplicit,        String isUnsettable,        String isResolveProxies,        String isDerived,        String defaultValueString,        String defaultValue,        String isComposite,        String isVolatile    ) {
        super(
        );
        this.isID = isID;
        this.isReadOnly = isReadOnly;
        this.isTransient = isTransient;
        this.isImplicit = isImplicit;
        this.isUnsettable = isUnsettable;
        this.isResolveProxies = isResolveProxies;
        this.isDerived = isDerived;
        this.defaultValueString = defaultValueString;
        this.defaultValue = defaultValue;
        this.isComposite = isComposite;
        this.isVolatile = isVolatile;
        this.pivot_propertys = new ArrayList<>();
    }

    public pivot_Property(
        String isID,        String isReadOnly,        String isTransient,        String isImplicit,        String isUnsettable,        String isResolveProxies,        String isDerived,        String defaultValueString,        String defaultValue,        String isComposite,        String isVolatile        ArrayList<pivot_Property> pivot_propertys    ) {
        this.isID = isID;
        this.isReadOnly = isReadOnly;
        this.isTransient = isTransient;
        this.isImplicit = isImplicit;
        this.isUnsettable = isUnsettable;
        this.isResolveProxies = isResolveProxies;
        this.isDerived = isDerived;
        this.defaultValueString = defaultValueString;
        this.defaultValue = defaultValue;
        this.isComposite = isComposite;
        this.isVolatile = isVolatile;
        this.pivot_propertys = pivot_propertys;
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
    public String getIsimplicit() {
        return isImplicit;
    }

    public void setIsimplicit(String isImplicit) {
        this.isImplicit = isImplicit;
    }
    public String getIsunsettable() {
        return isUnsettable;
    }

    public void setIsunsettable(String isUnsettable) {
        this.isUnsettable = isUnsettable;
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
    public String getDefaultvaluestring() {
        return defaultValueString;
    }

    public void setDefaultvaluestring(String defaultValueString) {
        this.defaultValueString = defaultValueString;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
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

    public pivot_AssociationClass getPivot_associationclass() {
        return pivot_associationclass;
    }

    public void setPivot_associationclass(pivot_AssociationClass pivot_associationclass) {
        this.pivot_associationclass = pivot_associationclass;
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
    public pivot_Class getPivot_class() {
        return pivot_class;
    }

    public void setPivot_class(pivot_Class pivot_class) {
        this.pivot_class = pivot_class;
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
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }

}