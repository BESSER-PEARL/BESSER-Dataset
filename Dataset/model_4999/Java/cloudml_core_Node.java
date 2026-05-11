





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Node extends WithProperties {

    private String imageID;
    private String securityGroup;
    private int minCore;
    private int minRam;
    private int minDisk;
    private String OS;
    private String location;
    private String privateKey;
    private String groupName;
    private String sshKey;
    private boolean is64os;



    public cloudml_core_Node(
        String imageID,        String securityGroup,        int minCore,        int minRam,        int minDisk,        String OS,        String location,        String privateKey,        String groupName,        String sshKey,        boolean is64os    ) {
        super(
        );
        this.imageID = imageID;
        this.securityGroup = securityGroup;
        this.minCore = minCore;
        this.minRam = minRam;
        this.minDisk = minDisk;
        this.OS = OS;
        this.location = location;
        this.privateKey = privateKey;
        this.groupName = groupName;
        this.sshKey = sshKey;
        this.is64os = is64os;
    }


    public String getImageid() {
        return imageID;
    }

    public void setImageid(String imageID) {
        this.imageID = imageID;
    }
    public String getSecuritygroup() {
        return securityGroup;
    }

    public void setSecuritygroup(String securityGroup) {
        this.securityGroup = securityGroup;
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
    public int getMindisk() {
        return minDisk;
    }

    public void setMindisk(int minDisk) {
        this.minDisk = minDisk;
    }
    public String getOs() {
        return OS;
    }

    public void setOs(String OS) {
        this.OS = OS;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
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


}