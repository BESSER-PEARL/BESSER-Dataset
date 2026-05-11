





import java.util.List;
import java.util.ArrayList;

public class cloudml_VM extends ExternalComponent {

    private int maxRam;
    private String providerSpecificTypeName;
    private String privateKey;
    private boolean is64os;
    private String groupName;
    private int maxStorage;
    private int minStorage;
    private int maxCores;
    private int minRam;
    private String sshKey;
    private String imageId;
    private int minCores;
    private String os;
    private String securityGroup;





    private cloudml_CloudMLModel cloudml_cloudmlmodel;




    private List<cloudml_VMPort> cloudml_vmports;


    public cloudml_VM(
        int maxRam,        String providerSpecificTypeName,        String privateKey,        boolean is64os,        String groupName,        int maxStorage,        int minStorage,        int maxCores,        int minRam,        String sshKey,        String imageId,        int minCores,        String os,        String securityGroup    ) {
        super(
        );
        this.maxRam = maxRam;
        this.providerSpecificTypeName = providerSpecificTypeName;
        this.privateKey = privateKey;
        this.is64os = is64os;
        this.groupName = groupName;
        this.maxStorage = maxStorage;
        this.minStorage = minStorage;
        this.maxCores = maxCores;
        this.minRam = minRam;
        this.sshKey = sshKey;
        this.imageId = imageId;
        this.minCores = minCores;
        this.os = os;
        this.securityGroup = securityGroup;
        this.cloudml_vmports = new ArrayList<>();
    }

    public cloudml_VM(
        int maxRam,        String providerSpecificTypeName,        String privateKey,        boolean is64os,        String groupName,        int maxStorage,        int minStorage,        int maxCores,        int minRam,        String sshKey,        String imageId,        int minCores,        String os,        String securityGroup        ArrayList<cloudml_VMPort> cloudml_vmports    ) {
        this.maxRam = maxRam;
        this.providerSpecificTypeName = providerSpecificTypeName;
        this.privateKey = privateKey;
        this.is64os = is64os;
        this.groupName = groupName;
        this.maxStorage = maxStorage;
        this.minStorage = minStorage;
        this.maxCores = maxCores;
        this.minRam = minRam;
        this.sshKey = sshKey;
        this.imageId = imageId;
        this.minCores = minCores;
        this.os = os;
        this.securityGroup = securityGroup;
        this.cloudml_vmports = cloudml_vmports;
    }

    public int getMaxram() {
        return maxRam;
    }

    public void setMaxram(int maxRam) {
        this.maxRam = maxRam;
    }
    public String getProviderspecifictypename() {
        return providerSpecificTypeName;
    }

    public void setProviderspecifictypename(String providerSpecificTypeName) {
        this.providerSpecificTypeName = providerSpecificTypeName;
    }
    public String getPrivatekey() {
        return privateKey;
    }

    public void setPrivatekey(String privateKey) {
        this.privateKey = privateKey;
    }
    public boolean getIs64os() {
        return is64os;
    }

    public void setIs64os(boolean is64os) {
        this.is64os = is64os;
    }
    public String getGroupname() {
        return groupName;
    }

    public void setGroupname(String groupName) {
        this.groupName = groupName;
    }
    public int getMaxstorage() {
        return maxStorage;
    }

    public void setMaxstorage(int maxStorage) {
        this.maxStorage = maxStorage;
    }
    public int getMinstorage() {
        return minStorage;
    }

    public void setMinstorage(int minStorage) {
        this.minStorage = minStorage;
    }
    public int getMaxcores() {
        return maxCores;
    }

    public void setMaxcores(int maxCores) {
        this.maxCores = maxCores;
    }
    public int getMinram() {
        return minRam;
    }

    public void setMinram(int minRam) {
        this.minRam = minRam;
    }
    public String getSshkey() {
        return sshKey;
    }

    public void setSshkey(String sshKey) {
        this.sshKey = sshKey;
    }
    public String getImageid() {
        return imageId;
    }

    public void setImageid(String imageId) {
        this.imageId = imageId;
    }
    public int getMincores() {
        return minCores;
    }

    public void setMincores(int minCores) {
        this.minCores = minCores;
    }
    public String getOs() {
        return os;
    }

    public void setOs(String os) {
        this.os = os;
    }
    public String getSecuritygroup() {
        return securityGroup;
    }

    public void setSecuritygroup(String securityGroup) {
        this.securityGroup = securityGroup;
    }

    public cloudml_CloudMLModel getCloudml_cloudmlmodel() {
        return cloudml_cloudmlmodel;
    }

    public void setCloudml_cloudmlmodel(cloudml_CloudMLModel cloudml_cloudmlmodel) {
        this.cloudml_cloudmlmodel = cloudml_cloudmlmodel;
    }
    public List<cloudml_VMPort> getCloudml_vmports() {
        return cloudml_vmports;
    }

    public void addCloudml_vmport(Cloudml_vmport cloudml_vmport) {
        this.cloudml_vmports.add(cloudml_vmport);
    }

}