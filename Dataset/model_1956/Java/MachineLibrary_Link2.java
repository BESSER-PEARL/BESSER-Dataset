





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_Link2  {

    private String link2ParamSection;
    private String link2ParamFile;
    private String link2Type;





    private MachineLibrary_LabMachine machinelibrary_labmachine;


    public MachineLibrary_Link2(
        String link2ParamSection,        String link2ParamFile,        String link2Type    ) {
        this.link2ParamSection = link2ParamSection;
        this.link2ParamFile = link2ParamFile;
        this.link2Type = link2Type;
    }


    public String getLink2paramsection() {
        return link2ParamSection;
    }

    public void setLink2paramsection(String link2ParamSection) {
        this.link2ParamSection = link2ParamSection;
    }
    public String getLink2paramfile() {
        return link2ParamFile;
    }

    public void setLink2paramfile(String link2ParamFile) {
        this.link2ParamFile = link2ParamFile;
    }
    public String getLink2type() {
        return link2Type;
    }

    public void setLink2type(String link2Type) {
        this.link2Type = link2Type;
    }

    public MachineLibrary_LabMachine getMachinelibrary_labmachine() {
        return machinelibrary_labmachine;
    }

    public void setMachinelibrary_labmachine(MachineLibrary_LabMachine machinelibrary_labmachine) {
        this.machinelibrary_labmachine = machinelibrary_labmachine;
    }

}