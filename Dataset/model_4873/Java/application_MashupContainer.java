





import java.util.List;
import java.util.ArrayList;

public class application_MashupContainer  {

    private String backupConfiguration;
    private String createAccountsAtLoginTry;
    private String immediateSave;
    private String backupIntervall;
    private String identCounter;





    private List<application_Interface> application_interfaces;




    private List<application_Mashup> application_mashups;




    private List<application_Mashup> application_mashups;




    private List<application_MashupAdmin> application_mashupadmins;




    private List<application_Mashup> application_mashups;


    public application_MashupContainer(
        String backupConfiguration,        String createAccountsAtLoginTry,        String immediateSave,        String backupIntervall,        String identCounter    ) {
        this.backupConfiguration = backupConfiguration;
        this.createAccountsAtLoginTry = createAccountsAtLoginTry;
        this.immediateSave = immediateSave;
        this.backupIntervall = backupIntervall;
        this.identCounter = identCounter;
        this.application_interfaces = new ArrayList<>();
        this.application_mashups = new ArrayList<>();
        this.application_mashups = new ArrayList<>();
        this.application_mashupadmins = new ArrayList<>();
        this.application_mashups = new ArrayList<>();
    }

    public application_MashupContainer(
        String backupConfiguration,        String createAccountsAtLoginTry,        String immediateSave,        String backupIntervall,        String identCounter        ArrayList<application_Interface> application_interfaces,        ArrayList<application_Mashup> application_mashups,        ArrayList<application_Mashup> application_mashups,        ArrayList<application_MashupAdmin> application_mashupadmins,        ArrayList<application_Mashup> application_mashups    ) {
        this.backupConfiguration = backupConfiguration;
        this.createAccountsAtLoginTry = createAccountsAtLoginTry;
        this.immediateSave = immediateSave;
        this.backupIntervall = backupIntervall;
        this.identCounter = identCounter;
        this.application_interfaces = application_interfaces;
        this.application_mashups = application_mashups;
        this.application_mashups = application_mashups;
        this.application_mashupadmins = application_mashupadmins;
        this.application_mashups = application_mashups;
    }

    public String getBackupconfiguration() {
        return backupConfiguration;
    }

    public void setBackupconfiguration(String backupConfiguration) {
        this.backupConfiguration = backupConfiguration;
    }
    public String getCreateaccountsatlogintry() {
        return createAccountsAtLoginTry;
    }

    public void setCreateaccountsatlogintry(String createAccountsAtLoginTry) {
        this.createAccountsAtLoginTry = createAccountsAtLoginTry;
    }
    public String getImmediatesave() {
        return immediateSave;
    }

    public void setImmediatesave(String immediateSave) {
        this.immediateSave = immediateSave;
    }
    public String getBackupintervall() {
        return backupIntervall;
    }

    public void setBackupintervall(String backupIntervall) {
        this.backupIntervall = backupIntervall;
    }
    public String getIdentcounter() {
        return identCounter;
    }

    public void setIdentcounter(String identCounter) {
        this.identCounter = identCounter;
    }

    public List<application_Interface> getApplication_interfaces() {
        return application_interfaces;
    }

    public void addApplication_interface(Application_interface application_interface) {
        this.application_interfaces.add(application_interface);
    }
    public List<application_Mashup> getApplication_mashups() {
        return application_mashups;
    }

    public void addApplication_mashup(Application_mashup application_mashup) {
        this.application_mashups.add(application_mashup);
    }
    public List<application_Mashup> getApplication_mashups() {
        return application_mashups;
    }

    public void addApplication_mashup(Application_mashup application_mashup) {
        this.application_mashups.add(application_mashup);
    }
    public List<application_MashupAdmin> getApplication_mashupadmins() {
        return application_mashupadmins;
    }

    public void addApplication_mashupadmin(Application_mashupadmin application_mashupadmin) {
        this.application_mashupadmins.add(application_mashupadmin);
    }
    public List<application_Mashup> getApplication_mashups() {
        return application_mashups;
    }

    public void addApplication_mashup(Application_mashup application_mashup) {
        this.application_mashups.add(application_mashup);
    }

}