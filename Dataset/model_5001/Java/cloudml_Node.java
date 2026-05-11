





import java.util.List;
import java.util.ArrayList;

public class cloudml_Node extends WithProperties {

    private String securityGroup;
    private String groupName;
    private String OS;
    private boolean is64os;
    private String location;
    private int minDisk;
    private int minCore;
    private String imageID;
    private String sshKey;
    private String privateKey;
    private int minRam;





    private cloudml_Provider cloudml_provider;


    public cloudml_Node(
        String securityGroup,        String groupName,        String OS,        boolean is64os,        String location,        int minDisk,        int minCore,        String imageID,        String sshKey,        String privateKey,        int minRam    ) {
        super(
        );
        this.securityGroup = securityGroup;
        this.groupName = groupName;
        this.OS = OS;
        this.is64os = is64os;
        this.location = location;
        this.minDisk = minDisk;
        this.minCore = minCore;
        this.imageID = imageID;
        this.sshKey = sshKey;
        this.privateKey = privateKey;
        this.minRam = minRam;
    }


    public String getSecuritygroup() {
        return securityGroup;
    }

    public void setSecuritygroup(String securityGroup) {
        this.securityGroup = securityGroup;
    }
    public String getGroupname() {
        return groupName;
    }

    public void setGroupname(String groupName) {
        this.groupName = groupName;
    }
    public String getOs() {
        return OS;
    }

    public void setOs(String OS) {
        this.OS = OS;
    }
    public boolean getIs64os() {
        return is64os;
    }

    public void setIs64os(boolean is64os) {
        this.is64os = is64os;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public int getMindisk() {
        return minDisk;
    }

    public void setMindisk(int minDisk) {
        this.minDisk = minDisk;
    }
    public int getMincore() {
        return minCore;
    }

    public void setMincore(int minCore) {
        this.minCore = minCore;
    }
    public String getImageid() {
        return imageID;
    }

    public void setImageid(String imageID) {
        this.imageID = imageID;
    }
    public String getSshkey() {
        return sshKey;
    }

    public void setSshkey(String sshKey) {
        this.sshKey = sshKey;
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

    public cloudml_Provider getCloudml_provider() {
        return cloudml_provider;
    }

    public void setCloudml_provider(cloudml_Provider cloudml_provider) {
        this.cloudml_provider = cloudml_provider;
    }

}