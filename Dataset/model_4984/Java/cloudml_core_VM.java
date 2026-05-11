





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_VM extends ExternalComponent {

    private String os;
    private int maxCores;
    private String privateKey;
    private boolean is64os;
    private int minStorage;
    private int maxRam;
    private String groupName;
    private int maxStorage;
    private int minRam;
    private String imageId;
    private int minCores;
    private String providerSpecificTypeName;
    private String securityGroup;
    private String sshKey;



    public cloudml_core_VM(
        String os,        int maxCores,        String privateKey,        boolean is64os,        int minStorage,        int maxRam,        String groupName,        int maxStorage,        int minRam,        String imageId,        int minCores,        String providerSpecificTypeName,        String securityGroup,        String sshKey    ) {
        super(
        );
        this.os = os;
        this.maxCores = maxCores;
        this.privateKey = privateKey;
        this.is64os = is64os;
        this.minStorage = minStorage;
        this.maxRam = maxRam;
        this.groupName = groupName;
        this.maxStorage = maxStorage;
        this.minRam = minRam;
        this.imageId = imageId;
        this.minCores = minCores;
        this.providerSpecificTypeName = providerSpecificTypeName;
        this.securityGroup = securityGroup;
        this.sshKey = sshKey;
    }


    public String getOs() {
        return os;
    }

    public void setOs(String os) {
        this.os = os;
    }
    public int getMaxcores() {
        return maxCores;
    }

    public void setMaxcores(int maxCores) {
        this.maxCores = maxCores;
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
    public int getMinstorage() {
        return minStorage;
    }

    public void setMinstorage(int minStorage) {
        this.minStorage = minStorage;
    }
    public int getMaxram() {
        return maxRam;
    }

    public void setMaxram(int maxRam) {
        this.maxRam = maxRam;
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
    public int getMinram() {
        return minRam;
    }

    public void setMinram(int minRam) {
        this.minRam = minRam;
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
    public String getProviderspecifictypename() {
        return providerSpecificTypeName;
    }

    public void setProviderspecifictypename(String providerSpecificTypeName) {
        this.providerSpecificTypeName = providerSpecificTypeName;
    }
    public String getSecuritygroup() {
        return securityGroup;
    }

    public void setSecuritygroup(String securityGroup) {
        this.securityGroup = securityGroup;
    }
    public String getSshkey() {
        return sshKey;
    }

    public void setSshkey(String sshKey) {
        this.sshKey = sshKey;
    }


}