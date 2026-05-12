





import java.util.List;
import java.util.ArrayList;

public class pivot_Property extends Feature {

    private String defaultValueString;
    private String isImplicit;
    private String isTransient;
    private String isID;
    private String isUnsettable;
    private String isComposite;
    private String isDerived;
    private String defaultValue;
    private String isVolatile;
    private String isReadOnly;
    private String isResolveProxies;





    private pivot_ShadowPart pivot_shadowpart;




    private pivot_Property pivot_property;




    private pivot_PropertyCallExp pivot_propertycallexp;




    private pivot_Slot pivot_slot;




    private pivot_Property pivot_property;




    private pivot_Class pivot_class;




    private pivot_Class pivot_class;




    private pivot_DynamicProperty pivot_dynamicproperty;




    private List<pivot_Property> pivot_propertys;




    private pivot_Property pivot_property;




    private pivot_LanguageExpression pivot_languageexpression;




    private pivot_Property pivot_property;


    public pivot_Property(
        String defaultValueString,        String isImplicit,        String isTransient,        String isID,        String isUnsettable,        String isComposite,        String isDerived,        String defaultValue,        String isVolatile,        String isReadOnly,        String isResolveProxies    ) {
        super(
        );
        this.defaultValueString = defaultValueString;
        this.isImplicit = isImplicit;
        this.isTransient = isTransient;
        this.isID = isID;
        this.isUnsettable = isUnsettable;
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.defaultValue = defaultValue;
        this.isVolatile = isVolatile;
        this.isReadOnly = isReadOnly;
        this.isResolveProxies = isResolveProxies;
        this.pivot_propertys = new ArrayList<>();
    }

    public pivot_Property(
        String defaultValueString,        String isImplicit,        String isTransient,        String isID,        String isUnsettable,        String isComposite,        String isDerived,        String defaultValue,        String isVolatile,        String isReadOnly,        String isResolveProxies        ArrayList<pivot_Property> pivot_propertys    ) {
        this.defaultValueString = defaultValueString;
        this.isImplicit = isImplicit;
        this.isTransient = isTransient;
        this.isID = isID;
        this.isUnsettable = isUnsettable;
        this.isComposite = isComposite;
        this.isDerived = isDerived;
        this.defaultValue = defaultValue;
        this.isVolatile = isVolatile;
        this.isReadOnly = isReadOnly;
        this.isResolveProxies = isResolveProxies;
        this.pivot_propertys = pivot_propertys;
    }

    public String getDefaultvaluestring() {
        return defaultValueString;
    }

    public void setDefaultvaluestring(String defaultValueString) {
        this.defaultValueString = defaultValueString;
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
    public String getIsid() {
        return isID;
    }

    public void setIsid(String isID) {
        this.isID = isID;
    }
    public String getIsunsettable() {
        return isUnsettable;
    }

    public void setIsunsettable(String isUnsettable) {
        this.isUnsettable = isUnsettable;
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
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
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
    public String getIsresolveproxies() {
        return isResolveProxies;
    }

    public void setIsresolveproxies(String isResolveProxies) {
        this.isResolveProxies = isResolveProxies;
    }

    public pivot_ShadowPart getPivot_shadowpart() {
        return pivot_shadowpart;
    }

    public void setPivot_shadowpart(pivot_ShadowPart pivot_shadowpart) {
        this.pivot_shadowpart = pivot_shadowpart;
    }
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }
    public pivot_PropertyCallExp getPivot_propertycallexp() {
        return pivot_propertycallexp;
    }

    public void setPivot_propertycallexp(pivot_PropertyCallExp pivot_propertycallexp) {
        this.pivot_propertycallexp = pivot_propertycallexp;
    }
    public pivot_Slot getPivot_slot() {
        return pivot_slot;
    }

    public void setPivot_slot(pivot_Slot pivot_slot) {
        this.pivot_slot = pivot_slot;
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
    public pivot_Class getPivot_class() {
        return pivot_class;
    }

    public void setPivot_class(pivot_Class pivot_class) {
        this.pivot_class = pivot_class;
    }
    public pivot_DynamicProperty getPivot_dynamicproperty() {
        return pivot_dynamicproperty;
    }

    public void setPivot_dynamicproperty(pivot_DynamicProperty pivot_dynamicproperty) {
        this.pivot_dynamicproperty = pivot_dynamicproperty;
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
    public pivot_LanguageExpression getPivot_languageexpression() {
        return pivot_languageexpression;
    }

    public void setPivot_languageexpression(pivot_LanguageExpression pivot_languageexpression) {
        this.pivot_languageexpression = pivot_languageexpression;
    }
    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }

}