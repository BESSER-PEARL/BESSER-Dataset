





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Node extends WithProperties {

    private String OS;
    private String securityGroup;
    private String location;
    private int minDisk;
    private boolean is64os;
    private int minCore;
    private int minRam;
    private String privateKey;
    private String groupName;
    private String imageID;
    private String sshKey;



    public cloudml_core_Node(
        String OS,        String securityGroup,        String location,        int minDisk,        boolean is64os,        int minCore,        int minRam,        String privateKey,        String groupName,        String imageID,        String sshKey    ) {
        super(
        );
        this.OS = OS;
        this.securityGroup = securityGroup;
        this.location = location;
        this.minDisk = minDisk;
        this.is64os = is64os;
        this.minCore = minCore;
        this.minRam = minRam;
        this.privateKey = privateKey;
        this.groupName = groupName;
        this.imageID = imageID;
        this.sshKey = sshKey;
    }


    public String getOs() {
        return OS;
    }

    public void setOs(String OS) {
        this.OS = OS;
    }
    public String getSecuritygroup() {
        return securityGroup;
    }

    public void setSecuritygroup(String securityGroup) {
        this.securityGroup = securityGroup;
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
    public boolean getIs64os() {
        return is64os;
    }

    public void setIs64os(boolean is64os) {
        this.is64os = is64os;
    }
    public int getMincore() {
        return minCore;
    }

    public void setMincore(int minCore) {
        this.minCore = minCore;
    }
    public int getMinram() {
        return minRam;
    }

    public void setMinram(int minRam) {
        this.minRam = minRam;
    }
    public String getPrivatekey() {
        return privateKey;
    }

    public void setPrivatekey(String privateKey) {
        this.privateKey = privateKey;
    }
    public String getGroupname() {
        return groupName;
    }

    public void setGroupname(String groupName) {
        this.groupName = groupName;
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


}