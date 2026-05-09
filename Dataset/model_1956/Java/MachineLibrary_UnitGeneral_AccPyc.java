





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_UnitGeneral_AccPyc  {

    private float cupWeight;
    private float minSampleWeight;





    private MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial;


    public MachineLibrary_UnitGeneral_AccPyc(
        float cupWeight,        float minSampleWeight    ) {
        this.cupWeight = cupWeight;
        this.minSampleWeight = minSampleWeight;
    }


    public float getCupweight() {
        return cupWeight;
    }

    public void setCupweight(float cupWeight) {
        this.cupWeight = cupWeight;
    }
    public float getMinsampleweight() {
        return minSampleWeight;
    }

    public void setMinsampleweight(float minSampleWeight) {
        this.minSampleWeight = minSampleWeight;
    }

    public MachineLibrary_UnitGeneralSpecial getMachinelibrary_unitgeneralspecial() {
        return machinelibrary_unitgeneralspecial;
    }

    public void setMachinelibrary_unitgeneralspecial(MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial) {
        this.machinelibrary_unitgeneralspecial = machinelibrary_unitgeneralspecial;
    }

}