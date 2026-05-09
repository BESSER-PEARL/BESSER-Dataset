





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_LabMachine  {

    private String driver;
    private String linkParamFile;
    private String linkParamSection;
    private String createWinCCTags;
    private String linkType;
    private String machineName;
    private float machineVersionNo;
    private String versionRemark;





    private MachineLibrary_LabMachines machinelibrary_labmachines;


    public MachineLibrary_LabMachine(
        String driver,        String linkParamFile,        String linkParamSection,        String createWinCCTags,        String linkType,        String machineName,        float machineVersionNo,        String versionRemark    ) {
        this.driver = driver;
        this.linkParamFile = linkParamFile;
        this.linkParamSection = linkParamSection;
        this.createWinCCTags = createWinCCTags;
        this.linkType = linkType;
        this.machineName = machineName;
        this.machineVersionNo = machineVersionNo;
        this.versionRemark = versionRemark;
    }


    public String getDriver() {
        return driver;
    }

    public void setDriver(String driver) {
        this.driver = driver;
    }
    public String getLinkparamfile() {
        return linkParamFile;
    }

    public void setLinkparamfile(String linkParamFile) {
        this.linkParamFile = linkParamFile;
    }
    public String getLinkparamsection() {
        return linkParamSection;
    }

    public void setLinkparamsection(String linkParamSection) {
        this.linkParamSection = linkParamSection;
    }
    public String getCreatewincctags() {
        return createWinCCTags;
    }

    public void setCreatewincctags(String createWinCCTags) {
        this.createWinCCTags = createWinCCTags;
    }
    public String getLinktype() {
        return linkType;
    }

    public void setLinktype(String linkType) {
        this.linkType = linkType;
    }
    public String getMachinename() {
        return machineName;
    }

    public void setMachinename(String machineName) {
        this.machineName = machineName;
    }
    public float getMachineversionno() {
        return machineVersionNo;
    }

    public void setMachineversionno(float machineVersionNo) {
        this.machineVersionNo = machineVersionNo;
    }
    public String getVersionremark() {
        return versionRemark;
    }

    public void setVersionremark(String versionRemark) {
        this.versionRemark = versionRemark;
    }

    public MachineLibrary_LabMachines getMachinelibrary_labmachines() {
        return machinelibrary_labmachines;
    }

    public void setMachinelibrary_labmachines(MachineLibrary_LabMachines machinelibrary_labmachines) {
        this.machinelibrary_labmachines = machinelibrary_labmachines;
    }

}