





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_UnitGeneral_SuperQ  {

    private int lastPosInInstrument;
    private int lastPosAnalysing;





    private MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial;


    public MachineLibrary_UnitGeneral_SuperQ(
        int lastPosInInstrument,        int lastPosAnalysing    ) {
        this.lastPosInInstrument = lastPosInInstrument;
        this.lastPosAnalysing = lastPosAnalysing;
    }


    public int getLastposininstrument() {
        return lastPosInInstrument;
    }

    public void setLastposininstrument(int lastPosInInstrument) {
        this.lastPosInInstrument = lastPosInInstrument;
    }
    public int getLastposanalysing() {
        return lastPosAnalysing;
    }

    public void setLastposanalysing(int lastPosAnalysing) {
        this.lastPosAnalysing = lastPosAnalysing;
    }

    public MachineLibrary_UnitGeneralSpecial getMachinelibrary_unitgeneralspecial() {
        return machinelibrary_unitgeneralspecial;
    }

    public void setMachinelibrary_unitgeneralspecial(MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial) {
        this.machinelibrary_unitgeneralspecial = machinelibrary_unitgeneralspecial;
    }

}