





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_UnitGeneral_Remote  {

    private String handshakeQ;
    private int handshakeT;
    private String handshakeA;
    private boolean editWSDB;





    private MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial;


    public MachineLibrary_UnitGeneral_Remote(
        String handshakeQ,        int handshakeT,        String handshakeA,        boolean editWSDB    ) {
        this.handshakeQ = handshakeQ;
        this.handshakeT = handshakeT;
        this.handshakeA = handshakeA;
        this.editWSDB = editWSDB;
    }


    public String getHandshakeq() {
        return handshakeQ;
    }

    public void setHandshakeq(String handshakeQ) {
        this.handshakeQ = handshakeQ;
    }
    public int getHandshaket() {
        return handshakeT;
    }

    public void setHandshaket(int handshakeT) {
        this.handshakeT = handshakeT;
    }
    public String getHandshakea() {
        return handshakeA;
    }

    public void setHandshakea(String handshakeA) {
        this.handshakeA = handshakeA;
    }
    public boolean getEditwsdb() {
        return editWSDB;
    }

    public void setEditwsdb(boolean editWSDB) {
        this.editWSDB = editWSDB;
    }

    public MachineLibrary_UnitGeneralSpecial getMachinelibrary_unitgeneralspecial() {
        return machinelibrary_unitgeneralspecial;
    }

    public void setMachinelibrary_unitgeneralspecial(MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial) {
        this.machinelibrary_unitgeneralspecial = machinelibrary_unitgeneralspecial;
    }

}