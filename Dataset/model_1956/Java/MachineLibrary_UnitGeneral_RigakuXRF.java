





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_UnitGeneral_RigakuXRF  {

    private int lastPoHAG_SIInstrument;
    private int lastPosAnalyHAG_SIg;
    private int separator;
    private int lastPosInInstrument;





    private MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial;


    public MachineLibrary_UnitGeneral_RigakuXRF(
        int lastPoHAG_SIInstrument,        int lastPosAnalyHAG_SIg,        int separator,        int lastPosInInstrument    ) {
        this.lastPoHAG_SIInstrument = lastPoHAG_SIInstrument;
        this.lastPosAnalyHAG_SIg = lastPosAnalyHAG_SIg;
        this.separator = separator;
        this.lastPosInInstrument = lastPosInInstrument;
    }


    public int getLastpohag_siinstrument() {
        return lastPoHAG_SIInstrument;
    }

    public void setLastpohag_siinstrument(int lastPoHAG_SIInstrument) {
        this.lastPoHAG_SIInstrument = lastPoHAG_SIInstrument;
    }
    public int getLastposanalyhag_sig() {
        return lastPosAnalyHAG_SIg;
    }

    public void setLastposanalyhag_sig(int lastPosAnalyHAG_SIg) {
        this.lastPosAnalyHAG_SIg = lastPosAnalyHAG_SIg;
    }
    public int getSeparator() {
        return separator;
    }

    public void setSeparator(int separator) {
        this.separator = separator;
    }
    public int getLastposininstrument() {
        return lastPosInInstrument;
    }

    public void setLastposininstrument(int lastPosInInstrument) {
        this.lastPosInInstrument = lastPosInInstrument;
    }

    public MachineLibrary_UnitGeneralSpecial getMachinelibrary_unitgeneralspecial() {
        return machinelibrary_unitgeneralspecial;
    }

    public void setMachinelibrary_unitgeneralspecial(MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial) {
        this.machinelibrary_unitgeneralspecial = machinelibrary_unitgeneralspecial;
    }

}