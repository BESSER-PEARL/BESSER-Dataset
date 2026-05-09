





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_UnitGeneral_Scanner  {

    private int forcedSampleType;
    private int start;
    private int registerSample;
    private String preString;
    private int length;
    private String fillWith;
    private String addString;





    private MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial;


    public MachineLibrary_UnitGeneral_Scanner(
        int forcedSampleType,        int start,        int registerSample,        String preString,        int length,        String fillWith,        String addString    ) {
        this.forcedSampleType = forcedSampleType;
        this.start = start;
        this.registerSample = registerSample;
        this.preString = preString;
        this.length = length;
        this.fillWith = fillWith;
        this.addString = addString;
    }


    public int getForcedsampletype() {
        return forcedSampleType;
    }

    public void setForcedsampletype(int forcedSampleType) {
        this.forcedSampleType = forcedSampleType;
    }
    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }
    public int getRegistersample() {
        return registerSample;
    }

    public void setRegistersample(int registerSample) {
        this.registerSample = registerSample;
    }
    public String getPrestring() {
        return preString;
    }

    public void setPrestring(String preString) {
        this.preString = preString;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getFillwith() {
        return fillWith;
    }

    public void setFillwith(String fillWith) {
        this.fillWith = fillWith;
    }
    public String getAddstring() {
        return addString;
    }

    public void setAddstring(String addString) {
        this.addString = addString;
    }

    public MachineLibrary_UnitGeneralSpecial getMachinelibrary_unitgeneralspecial() {
        return machinelibrary_unitgeneralspecial;
    }

    public void setMachinelibrary_unitgeneralspecial(MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial) {
        this.machinelibrary_unitgeneralspecial = machinelibrary_unitgeneralspecial;
    }

}