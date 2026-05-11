





import java.util.List;
import java.util.ArrayList;

public class cloudml_Node extends WithProperties {

    private String OS;
    private String sshKey;
    private boolean is64os;
    private String location;
    private String privateKey;
    private String securityGroup;
    private String groupName;
    private int minRam;
    private String imageID;
    private int minCore;
    private int minDisk;



    public cloudml_Node(
        String OS,        String sshKey,        boolean is64os,        String location,        String privateKey,        String securityGroup,        String groupName,        int minRam,        String imageID,        int minCore,        int minDisk    ) {
        super(
        );
        this.OS = OS;
        this.sshKey = sshKey;
        this.is64os = is64os;
        this.location = location;
        this.privateKey = privateKey;
        this.securityGroup = securityGroup;
        this.groupName = groupName;
        this.minRam = minRam;
        this.imageID = imageID;
        this.minCore = minCore;
        this.minDisk = minDisk;
    }


    public String getOs() {
        return OS;
    }

    public void setOs(String OS) {
        this.OS = OS;
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
    public int getMincore() {
        return minCore;
    }

    public void setMincore(int minCore) {
        this.minCore = minCore;
    }
    public int getMindisk() {
        return minDisk;
    }

    public void setMindisk(int minDisk) {
        this.minDisk = minDisk;
    }


}