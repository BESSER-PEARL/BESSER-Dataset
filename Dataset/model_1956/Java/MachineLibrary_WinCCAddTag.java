





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_WinCCAddTag  {

    private String winCCTag;





    private MachineLibrary_NodeGeneral_WinCC2WinCC machinelibrary_nodegeneral_wincc2wincc;


    public MachineLibrary_WinCCAddTag(
        String winCCTag    ) {
        this.winCCTag = winCCTag;
    }


    public String getWincctag() {
        return winCCTag;
    }

    public void setWincctag(String winCCTag) {
        this.winCCTag = winCCTag;
    }

    public MachineLibrary_NodeGeneral_WinCC2WinCC getMachinelibrary_nodegeneral_wincc2wincc() {
        return machinelibrary_nodegeneral_wincc2wincc;
    }

    public void setMachinelibrary_nodegeneral_wincc2wincc(MachineLibrary_NodeGeneral_WinCC2WinCC machinelibrary_nodegeneral_wincc2wincc) {
        this.machinelibrary_nodegeneral_wincc2wincc = machinelibrary_nodegeneral_wincc2wincc;
    }

}