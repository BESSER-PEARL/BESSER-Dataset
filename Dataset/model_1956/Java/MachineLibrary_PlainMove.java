





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_PlainMove  {

    private int plainmoveType;
    private String plainmoveSID_REF;
    private String plainmovePreDefWS;





    private MachineLibrary_NodeSpecialConfiguration machinelibrary_nodespecialconfiguration;


    public MachineLibrary_PlainMove(
        int plainmoveType,        String plainmoveSID_REF,        String plainmovePreDefWS    ) {
        this.plainmoveType = plainmoveType;
        this.plainmoveSID_REF = plainmoveSID_REF;
        this.plainmovePreDefWS = plainmovePreDefWS;
    }


    public int getPlainmovetype() {
        return plainmoveType;
    }

    public void setPlainmovetype(int plainmoveType) {
        this.plainmoveType = plainmoveType;
    }
    public String getPlainmovesid_ref() {
        return plainmoveSID_REF;
    }

    public void setPlainmovesid_ref(String plainmoveSID_REF) {
        this.plainmoveSID_REF = plainmoveSID_REF;
    }
    public String getPlainmovepredefws() {
        return plainmovePreDefWS;
    }

    public void setPlainmovepredefws(String plainmovePreDefWS) {
        this.plainmovePreDefWS = plainmovePreDefWS;
    }

    public MachineLibrary_NodeSpecialConfiguration getMachinelibrary_nodespecialconfiguration() {
        return machinelibrary_nodespecialconfiguration;
    }

    public void setMachinelibrary_nodespecialconfiguration(MachineLibrary_NodeSpecialConfiguration machinelibrary_nodespecialconfiguration) {
        this.machinelibrary_nodespecialconfiguration = machinelibrary_nodespecialconfiguration;
    }

}