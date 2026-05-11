





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_VM extends ExternalComponent {

    private String imageId;
    private String privateKey;
    private int maxRam;
    private int minRam;
    private boolean is64os;
    private String sshKey;
    private String securityGroup;
    private int minStorage;
    private int maxStorage;
    private String groupName;
    private int maxCores;
    private int minCores;
    private String os;
    private String providerSpecificTypeName;



    public cloudml_core_VM(
        String imageId,        String privateKey,        int maxRam,        int minRam,        boolean is64os,        String sshKey,        String securityGroup,        int minStorage,        int maxStorage,        String groupName,        int maxCores,        int minCores,        String os,        String providerSpecificTypeName    ) {
        super(
        );
        this.imageId = imageId;
        this.privateKey = privateKey;
        this.maxRam = maxRam;
        this.minRam = minRam;
        this.is64os = is64os;
        this.sshKey = sshKey;
        this.securityGroup = securityGroup;
        this.minStorage = minStorage;
        this.maxStorage = maxStorage;
        this.groupName = groupName;
        this.maxCores = maxCores;
        this.minCores = minCores;
        this.os = os;
        this.providerSpecificTypeName = providerSpecificTypeName;
    }


    public String getImageid() {
        return imageId;
    }

    public void setImageid(String imageId) {
        this.imageId = imageId;
    }
    public String getPrivatekey() {
        return privateKey;
    }

    public void setPrivatekey(String privateKey) {
        this.privateKey = privateKey;
    }
    public int getMaxram() {
        return maxRam;
    }

    public void setMaxram(int maxRam) {
        this.maxRam = maxRam;
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
    public String getSshkey() {
        return sshKey;
    }

    public void setSshkey(String sshKey) {
        this.sshKey = sshKey;
    }
    public String getSecuritygroup() {
        return securityGroup;
    }

    public void setSecuritygroup(String securityGroup) {
        this.securityGroup = securityGroup;
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
    public String getGroupname() {
        return groupName;
    }

    public void setGroupname(String groupName) {
        this.groupName = groupName;
    }
    public int getMaxcores() {
        return maxCores;
    }

    public void setMaxcores(int maxCores) {
        this.maxCores = maxCores;
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
    public String getProviderspecifictypename() {
        return providerSpecificTypeName;
    }

    public void setProviderspecifictypename(String providerSpecificTypeName) {
        this.providerSpecificTypeName = providerSpecificTypeName;
    }


}