





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Node extends WithProperties {

    private String OS;
    private String groupName;
    private boolean is64os;
    private int minCore;
    private String sshKey;
    private String securityGroup;
    private String location;
    private String privateKey;
    private String imageID;
    private int minDisk;
    private int minRam;



    public cloudml_core_Node(
        String OS,        String groupName,        boolean is64os,        int minCore,        String sshKey,        String securityGroup,        String location,        String privateKey,        String imageID,        int minDisk,        int minRam    ) {
        super(
        );
        this.OS = OS;
        this.groupName = groupName;
        this.is64os = is64os;
        this.minCore = minCore;
        this.sshKey = sshKey;
        this.securityGroup = securityGroup;
        this.location = location;
        this.privateKey = privateKey;
        this.imageID = imageID;
        this.minDisk = minDisk;
        this.minRam = minRam;
    }


    public String getOs() {
        return OS;
    }

    public void setOs(String OS) {
        this.OS = OS;
    }
    public String getGroupname() {
        return groupName;
    }

    public void setGroupname(String groupName) {
        this.groupName = groupName;
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
    public String getImageid() {
        return imageID;
    }

    public void setImageid(String imageID) {
        this.imageID = imageID;
    }
    public int getMindisk() {
        return minDisk;
    }

    public void setMindisk(int minDisk) {
        this.minDisk = minDisk;
    }
    public int getMinram() {
        return minRam;
    }

    public void setMinram(int minRam) {
        this.minRam = minRam;
    }


}