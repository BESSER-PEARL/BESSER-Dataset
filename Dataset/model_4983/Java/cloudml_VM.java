





import java.util.List;
import java.util.ArrayList;

public class cloudml_VM extends ExternalComponent {

    private String providerSpecificTypeName;
    private String privateKey;
    private String os;
    private int minRam;
    private boolean is64os;
    private int minStorage;
    private int maxStorage;
    private String imageId;
    private String groupName;
    private int maxRam;
    private int minCores;
    private String securityGroup;
    private int maxCores;
    private String sshKey;





    private cloudml_CloudMLModel cloudml_cloudmlmodel;




    private List<cloudml_VMPort> cloudml_vmports;


    public cloudml_VM(
        String providerSpecificTypeName,        String privateKey,        String os,        int minRam,        boolean is64os,        int minStorage,        int maxStorage,        String imageId,        String groupName,        int maxRam,        int minCores,        String securityGroup,        int maxCores,        String sshKey    ) {
        super(
        );
        this.providerSpecificTypeName = providerSpecificTypeName;
        this.privateKey = privateKey;
        this.os = os;
        this.minRam = minRam;
        this.is64os = is64os;
        this.minStorage = minStorage;
        this.maxStorage = maxStorage;
        this.imageId = imageId;
        this.groupName = groupName;
        this.maxRam = maxRam;
        this.minCores = minCores;
        this.securityGroup = securityGroup;
        this.maxCores = maxCores;
        this.sshKey = sshKey;
        this.cloudml_vmports = new ArrayList<>();
    }

    public cloudml_VM(
        String providerSpecificTypeName,        String privateKey,        String os,        int minRam,        boolean is64os,        int minStorage,        int maxStorage,        String imageId,        String groupName,        int maxRam,        int minCores,        String securityGroup,        int maxCores,        String sshKey        ArrayList<cloudml_VMPort> cloudml_vmports    ) {
        this.providerSpecificTypeName = providerSpecificTypeName;
        this.privateKey = privateKey;
        this.os = os;
        this.minRam = minRam;
        this.is64os = is64os;
        this.minStorage = minStorage;
        this.maxStorage = maxStorage;
        this.imageId = imageId;
        this.groupName = groupName;
        this.maxRam = maxRam;
        this.minCores = minCores;
        this.securityGroup = securityGroup;
        this.maxCores = maxCores;
        this.sshKey = sshKey;
        this.cloudml_vmports = cloudml_vmports;
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
    public String getOs() {
        return os;
    }

    public void setOs(String os) {
        this.os = os;
    }
    public int getMinram() {
        return minRam;
    }

    public void setMinram(int minRam) {
        this.minRam = minRam;
    }
    public boolean getIs64os() {
        return is64os;
    }

    public void setIs64os(boolean is64os) {
        this.is64os = is64os;
    }
    public int getMinstorage() {
        return minStorage;
    }

    public void setMinstorage(int minStorage) {
        this.minStorage = minStorage;
    }
    public int getMaxstorage() {
        return maxStorage;
    }

    public void setMaxstorage(int maxStorage) {
        this.maxStorage = maxStorage;
    }
    public String getImageid() {
        return imageId;
    }

    public void setImageid(String imageId) {
        this.imageId = imageId;
    }
    public String getGroupname() {
        return groupName;
    }

    public void setGroupname(String groupName) {
        this.groupName = groupName;
    }
    public int getMaxram() {
        return maxRam;
    }

    public void setMaxram(int maxRam) {
        this.maxRam = maxRam;
    }
    public int getMincores() {
        return minCores;
    }

    public void setMincores(int minCores) {
        this.minCores = minCores;
    }
    public String getSecuritygroup() {
        return securityGroup;
    }

    public void setSecuritygroup(String securityGroup) {
        this.securityGroup = securityGroup;
    }
    public int getMaxcores() {
        return maxCores;
    }

    public void setMaxcores(int maxCores) {
        this.maxCores = maxCores;
    }
    public String getSshkey() {
        return sshKey;
    }

    public void setSshkey(String sshKey) {
        this.sshKey = sshKey;
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