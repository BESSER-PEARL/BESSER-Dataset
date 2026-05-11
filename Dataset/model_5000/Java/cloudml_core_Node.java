





import java.util.List;
import java.util.ArrayList;

public class cloudml_core_Node extends WithProperties {

    private String location;
    private String privateKey;
    private boolean is64os;
    private String groupName;
    private String OS;
    private int minDisk;
    private String securityGroup;
    private String sshKey;
    private int minCore;
    private int minRam;
    private String imageID;



    public cloudml_core_Node(
        String location,        String privateKey,        boolean is64os,        String groupName,        String OS,        int minDisk,        String securityGroup,        String sshKey,        int minCore,        int minRam,        String imageID    ) {
        super(
        );
        this.location = location;
        this.privateKey = privateKey;
        this.is64os = is64os;
        this.groupName = groupName;
        this.OS = OS;
        this.minDisk = minDisk;
        this.securityGroup = securityGroup;
        this.sshKey = sshKey;
        this.minCore = minCore;
        this.minRam = minRam;
        this.imageID = imageID;
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
    public String getOs() {
        return OS;
    }

    public void setOs(String OS) {
        this.OS = OS;
    }
    public int getMindisk() {
        return minDisk;
    }

    public void setMindisk(int minDisk) {
        this.minDisk = minDisk;
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
    public String getImageid() {
        return imageID;
    }

    public void setImageid(String imageID) {
        this.imageID = imageID;
    }


}