





import java.util.List;
import java.util.ArrayList;

public class ccore_ItemType extends TypeDefinition {

    private String packageName;
    private String itemFactoryClass;
    private String managerClass;
    private String itemManagerClass;
    private boolean isRootElement;
    private boolean hasContent;
    private boolean overwriteDefaultPages;
    private String icon;
    private String messageErrorId;
    private boolean isInstanceHidden;
    private boolean hasUniqueName;
    private String displayNameTemplate;
    private boolean hasShortName;
    private boolean isMetaItemType;
    private String validateNameRe;
    private boolean isInstanceAbstract;
    private boolean customManager;
    private String humanName;
    private String qualifiedNameTemplate;





    private List<ccore_ItemType> ccore_itemtypes;




    private List<ccore_ExtentedType> ccore_extentedtypes;




    private List<ccore_ItemType> ccore_itemtypes;




    private ccore_ExtentedType ccore_extentedtype;


    public ccore_ItemType(
        String packageName,        String itemFactoryClass,        String managerClass,        String itemManagerClass,        boolean isRootElement,        boolean hasContent,        boolean overwriteDefaultPages,        String icon,        String messageErrorId,        boolean isInstanceHidden,        boolean hasUniqueName,        String displayNameTemplate,        boolean hasShortName,        boolean isMetaItemType,        String validateNameRe,        boolean isInstanceAbstract,        boolean customManager,        String humanName,        String qualifiedNameTemplate    ) {
        super(
        );
        this.packageName = packageName;
        this.itemFactoryClass = itemFactoryClass;
        this.managerClass = managerClass;
        this.itemManagerClass = itemManagerClass;
        this.isRootElement = isRootElement;
        this.hasContent = hasContent;
        this.overwriteDefaultPages = overwriteDefaultPages;
        this.icon = icon;
        this.messageErrorId = messageErrorId;
        this.isInstanceHidden = isInstanceHidden;
        this.hasUniqueName = hasUniqueName;
        this.displayNameTemplate = displayNameTemplate;
        this.hasShortName = hasShortName;
        this.isMetaItemType = isMetaItemType;
        this.validateNameRe = validateNameRe;
        this.isInstanceAbstract = isInstanceAbstract;
        this.customManager = customManager;
        this.humanName = humanName;
        this.qualifiedNameTemplate = qualifiedNameTemplate;
        this.ccore_itemtypes = new ArrayList<>();
        this.ccore_extentedtypes = new ArrayList<>();
        this.ccore_itemtypes = new ArrayList<>();
    }

    public ccore_ItemType(
        String packageName,        String itemFactoryClass,        String managerClass,        String itemManagerClass,        boolean isRootElement,        boolean hasContent,        boolean overwriteDefaultPages,        String icon,        String messageErrorId,        boolean isInstanceHidden,        boolean hasUniqueName,        String displayNameTemplate,        boolean hasShortName,        boolean isMetaItemType,        String validateNameRe,        boolean isInstanceAbstract,        boolean customManager,        String humanName,        String qualifiedNameTemplate        ArrayList<ccore_ItemType> ccore_itemtypes,        ArrayList<ccore_ExtentedType> ccore_extentedtypes,        ArrayList<ccore_ItemType> ccore_itemtypes    ) {
        this.packageName = packageName;
        this.itemFactoryClass = itemFactoryClass;
        this.managerClass = managerClass;
        this.itemManagerClass = itemManagerClass;
        this.isRootElement = isRootElement;
        this.hasContent = hasContent;
        this.overwriteDefaultPages = overwriteDefaultPages;
        this.icon = icon;
        this.messageErrorId = messageErrorId;
        this.isInstanceHidden = isInstanceHidden;
        this.hasUniqueName = hasUniqueName;
        this.displayNameTemplate = displayNameTemplate;
        this.hasShortName = hasShortName;
        this.isMetaItemType = isMetaItemType;
        this.validateNameRe = validateNameRe;
        this.isInstanceAbstract = isInstanceAbstract;
        this.customManager = customManager;
        this.humanName = humanName;
        this.qualifiedNameTemplate = qualifiedNameTemplate;
        this.ccore_itemtypes = ccore_itemtypes;
        this.ccore_extentedtypes = ccore_extentedtypes;
        this.ccore_itemtypes = ccore_itemtypes;
    }

    public String getPackagename() {
        return packageName;
    }

    public void setPackagename(String packageName) {
        this.packageName = packageName;
    }
    public String getItemfactoryclass() {
        return itemFactoryClass;
    }

    public void setItemfactoryclass(String itemFactoryClass) {
        this.itemFactoryClass = itemFactoryClass;
    }
    public String getManagerclass() {
        return managerClass;
    }

    public void setManagerclass(String managerClass) {
        this.managerClass = managerClass;
    }
    public String getItemmanagerclass() {
        return itemManagerClass;
    }

    public void setItemmanagerclass(String itemManagerClass) {
        this.itemManagerClass = itemManagerClass;
    }
    public boolean getIsrootelement() {
        return isRootElement;
    }

    public void setIsrootelement(boolean isRootElement) {
        this.isRootElement = isRootElement;
    }
    public boolean getHascontent() {
        return hasContent;
    }

    public void setHascontent(boolean hasContent) {
        this.hasContent = hasContent;
    }
    public boolean getOverwritedefaultpages() {
        return overwriteDefaultPages;
    }

    public void setOverwritedefaultpages(boolean overwriteDefaultPages) {
        this.overwriteDefaultPages = overwriteDefaultPages;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getMessageerrorid() {
        return messageErrorId;
    }

    public void setMessageerrorid(String messageErrorId) {
        this.messageErrorId = messageErrorId;
    }
    public boolean getIsinstancehidden() {
        return isInstanceHidden;
    }

    public void setIsinstancehidden(boolean isInstanceHidden) {
        this.isInstanceHidden = isInstanceHidden;
    }
    public boolean getHasuniquename() {
        return hasUniqueName;
    }

    public void setHasuniquename(boolean hasUniqueName) {
        this.hasUniqueName = hasUniqueName;
    }
    public String getDisplaynametemplate() {
        return displayNameTemplate;
    }

    public void setDisplaynametemplate(String displayNameTemplate) {
        this.displayNameTemplate = displayNameTemplate;
    }
    public boolean getHasshortname() {
        return hasShortName;
    }

    public void setHasshortname(boolean hasShortName) {
        this.hasShortName = hasShortName;
    }
    public boolean getIsmetaitemtype() {
        return isMetaItemType;
    }

    public void setIsmetaitemtype(boolean isMetaItemType) {
        this.isMetaItemType = isMetaItemType;
    }
    public String getValidatenamere() {
        return validateNameRe;
    }

    public void setValidatenamere(String validateNameRe) {
        this.validateNameRe = validateNameRe;
    }
    public boolean getIsinstanceabstract() {
        return isInstanceAbstract;
    }

    public void setIsinstanceabstract(boolean isInstanceAbstract) {
        this.isInstanceAbstract = isInstanceAbstract;
    }
    public boolean getCustommanager() {
        return customManager;
    }

    public void setCustommanager(boolean customManager) {
        this.customManager = customManager;
    }
    public String getHumanname() {
        return humanName;
    }

    public void setHumanname(String humanName) {
        this.humanName = humanName;
    }
    public String getQualifiednametemplate() {
        return qualifiedNameTemplate;
    }

    public void setQualifiednametemplate(String qualifiedNameTemplate) {
        this.qualifiedNameTemplate = qualifiedNameTemplate;
    }

    public List<ccore_ItemType> getCcore_itemtypes() {
        return ccore_itemtypes;
    }

    public void addCcore_itemtype(Ccore_itemtype ccore_itemtype) {
        this.ccore_itemtypes.add(ccore_itemtype);
    }
    public List<ccore_ExtentedType> getCcore_extentedtypes() {
        return ccore_extentedtypes;
    }

    public void addCcore_extentedtype(Ccore_extentedtype ccore_extentedtype) {
        this.ccore_extentedtypes.add(ccore_extentedtype);
    }
    public List<ccore_ItemType> getCcore_itemtypes() {
        return ccore_itemtypes;
    }

    public void addCcore_itemtype(Ccore_itemtype ccore_itemtype) {
        this.ccore_itemtypes.add(ccore_itemtype);
    }
    public ccore_ExtentedType getCcore_extentedtype() {
        return ccore_extentedtype;
    }

    public void setCcore_extentedtype(ccore_ExtentedType ccore_extentedtype) {
        this.ccore_extentedtype = ccore_extentedtype;
    }

}