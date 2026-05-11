





import java.util.List;
import java.util.ArrayList;

public class ccore_Cadse extends EPackage, Item {

    private String defaultContentRepoURL;
    private String description;
    private String idDefinition;
    private String itemRepoLogin;
    private String itemRepoURL;
    private boolean executed;
    private String itemRepoPasswd;





    private ccore_EPackage ccore_epackage;




    private List<ccore_ItemType> ccore_itemtypes;




    private List<ccore_KeyDefinition> ccore_keydefinitions;




    private List<ccore_Cadse> ccore_cadses;




    private List<ccore_ExtentedType> ccore_extentedtypes;


    public ccore_Cadse(
        String defaultContentRepoURL,        String description,        String idDefinition,        String itemRepoLogin,        String itemRepoURL,        boolean executed,        String itemRepoPasswd    ) {
        super(
        );
        this.defaultContentRepoURL = defaultContentRepoURL;
        this.description = description;
        this.idDefinition = idDefinition;
        this.itemRepoLogin = itemRepoLogin;
        this.itemRepoURL = itemRepoURL;
        this.executed = executed;
        this.itemRepoPasswd = itemRepoPasswd;
        this.ccore_itemtypes = new ArrayList<>();
        this.ccore_keydefinitions = new ArrayList<>();
        this.ccore_cadses = new ArrayList<>();
        this.ccore_extentedtypes = new ArrayList<>();
    }

    public ccore_Cadse(
        String defaultContentRepoURL,        String description,        String idDefinition,        String itemRepoLogin,        String itemRepoURL,        boolean executed,        String itemRepoPasswd        ArrayList<ccore_ItemType> ccore_itemtypes,        ArrayList<ccore_KeyDefinition> ccore_keydefinitions,        ArrayList<ccore_Cadse> ccore_cadses,        ArrayList<ccore_ExtentedType> ccore_extentedtypes    ) {
        this.defaultContentRepoURL = defaultContentRepoURL;
        this.description = description;
        this.idDefinition = idDefinition;
        this.itemRepoLogin = itemRepoLogin;
        this.itemRepoURL = itemRepoURL;
        this.executed = executed;
        this.itemRepoPasswd = itemRepoPasswd;
        this.ccore_itemtypes = ccore_itemtypes;
        this.ccore_keydefinitions = ccore_keydefinitions;
        this.ccore_cadses = ccore_cadses;
        this.ccore_extentedtypes = ccore_extentedtypes;
    }

    public String getDefaultcontentrepourl() {
        return defaultContentRepoURL;
    }

    public void setDefaultcontentrepourl(String defaultContentRepoURL) {
        this.defaultContentRepoURL = defaultContentRepoURL;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getIddefinition() {
        return idDefinition;
    }

    public void setIddefinition(String idDefinition) {
        this.idDefinition = idDefinition;
    }
    public String getItemrepologin() {
        return itemRepoLogin;
    }

    public void setItemrepologin(String itemRepoLogin) {
        this.itemRepoLogin = itemRepoLogin;
    }
    public String getItemrepourl() {
        return itemRepoURL;
    }

    public void setItemrepourl(String itemRepoURL) {
        this.itemRepoURL = itemRepoURL;
    }
    public boolean getExecuted() {
        return executed;
    }

    public void setExecuted(boolean executed) {
        this.executed = executed;
    }
    public String getItemrepopasswd() {
        return itemRepoPasswd;
    }

    public void setItemrepopasswd(String itemRepoPasswd) {
        this.itemRepoPasswd = itemRepoPasswd;
    }

    public ccore_EPackage getCcore_epackage() {
        return ccore_epackage;
    }

    public void setCcore_epackage(ccore_EPackage ccore_epackage) {
        this.ccore_epackage = ccore_epackage;
    }
    public List<ccore_ItemType> getCcore_itemtypes() {
        return ccore_itemtypes;
    }

    public void addCcore_itemtype(Ccore_itemtype ccore_itemtype) {
        this.ccore_itemtypes.add(ccore_itemtype);
    }
    public List<ccore_KeyDefinition> getCcore_keydefinitions() {
        return ccore_keydefinitions;
    }

    public void addCcore_keydefinition(Ccore_keydefinition ccore_keydefinition) {
        this.ccore_keydefinitions.add(ccore_keydefinition);
    }
    public List<ccore_Cadse> getCcore_cadses() {
        return ccore_cadses;
    }

    public void addCcore_cadse(Ccore_cadse ccore_cadse) {
        this.ccore_cadses.add(ccore_cadse);
    }
    public List<ccore_ExtentedType> getCcore_extentedtypes() {
        return ccore_extentedtypes;
    }

    public void addCcore_extentedtype(Ccore_extentedtype ccore_extentedtype) {
        this.ccore_extentedtypes.add(ccore_extentedtype);
    }

}