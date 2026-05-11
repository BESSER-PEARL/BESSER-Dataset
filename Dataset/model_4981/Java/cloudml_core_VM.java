





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_VM extends ExternalComponent {

    private int minRam;
    private String sshKey;
    private boolean is64os;
    private String privateKey;
    private String imageId;
    private int maxRam;
    private int minStorage;
    private int maxStorage;
    private String securityGroup;
    private String os;
    private String groupName;
    private int maxCores;
    private int minCores;
    private String providerSpecificTypeName;



    public cloudml_core_VM(
        int minRam,        String sshKey,        boolean is64os,        String privateKey,        String imageId,        int maxRam,        int minStorage,        int maxStorage,        String securityGroup,        String os,        String groupName,        int maxCores,        int minCores,        String providerSpecificTypeName    ) {
        super(
        );
        this.minRam = minRam;
        this.sshKey = sshKey;
        this.is64os = is64os;
        this.privateKey = privateKey;
        this.imageId = imageId;
        this.maxRam = maxRam;
        this.minStorage = minStorage;
        this.maxStorage = maxStorage;
        this.securityGroup = securityGroup;
        this.os = os;
        this.groupName = groupName;
        this.maxCores = maxCores;
        this.minCores = minCores;
        this.providerSpecificTypeName = providerSpecificTypeName;
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
    public boolean getIs64os() {
        return is64os;
    }

    public void setIs64os(boolean is64os) {
        this.is64os = is64os;
    }
    public String getPrivatekey() {
        return privateKey;
    }

    public void setPrivatekey(String privateKey) {
        this.privateKey = privateKey;
    }
    public String getImageid() {
        return imageId;
    }

    public void setImageid(String imageId) {
        this.imageId = imageId;
    }
    public int getMaxram() {
        return maxRam;
    }

    public void setMaxram(int maxRam) {
        this.maxRam = maxRam;
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
    public String getSecuritygroup() {
        return securityGroup;
    }

    public void setSecuritygroup(String securityGroup) {
        this.securityGroup = securityGroup;
    }
    public String getOs() {
        return os;
    }

    public void setOs(String os) {
        this.os = os;
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
    public String getProviderspecifictypename() {
        return providerSpecificTypeName;
    }

    public void setProviderspecifictypename(String providerSpecificTypeName) {
        this.providerSpecificTypeName = providerSpecificTypeName;
    }


}