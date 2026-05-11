





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_VM extends ExternalComponent {

    private int maxCores;
    private String imageId;
    private int maxRam;
    private String privateKey;
    private int minRam;
    private int maxStorage;
    private String os;
    private String sshKey;
    private int minCores;
    private boolean is64os;
    private String securityGroup;
    private int minStorage;
    private String groupName;



    public cloudml_core_VM(
        int maxCores,        String imageId,        int maxRam,        String privateKey,        int minRam,        int maxStorage,        String os,        String sshKey,        int minCores,        boolean is64os,        String securityGroup,        int minStorage,        String groupName    ) {
        super(
        );
        this.maxCores = maxCores;
        this.imageId = imageId;
        this.maxRam = maxRam;
        this.privateKey = privateKey;
        this.minRam = minRam;
        this.maxStorage = maxStorage;
        this.os = os;
        this.sshKey = sshKey;
        this.minCores = minCores;
        this.is64os = is64os;
        this.securityGroup = securityGroup;
        this.minStorage = minStorage;
        this.groupName = groupName;
    }


    public int getMaxcores() {
        return maxCores;
    }

    public void setMaxcores(int maxCores) {
        this.maxCores = maxCores;
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
    public String getPrivatekey() {
        return privateKey;
    }

    public void setPrivatekey(String privateKey) {
        this.privateKey = privateKey;
    }
    public int getMinram() {
        return minRam;
    }

    public void setMinram(int minRam) {
        this.minRam = minRam;
    }
    public int getMaxstorage() {
        return maxStorage;
    }

    public void setMaxstorage(int maxStorage) {
        this.maxStorage = maxStorage;
    }
    public String getOs() {
        return os;
    }

    public void setOs(String os) {
        this.os = os;
    }
    public String getSshkey() {
        return sshKey;
    }

    public void setSshkey(String sshKey) {
        this.sshKey = sshKey;
    }
    public int getMincores() {
        return minCores;
    }

    public void setMincores(int minCores) {
        this.minCores = minCores;
    }
    public boolean getIs64os() {
        return is64os;
    }

    public void setIs64os(boolean is64os) {
        this.is64os = is64os;
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
    public String getGroupname() {
        return groupName;
    }

    public void setGroupname(String groupName) {
        this.groupName = groupName;
    }


}