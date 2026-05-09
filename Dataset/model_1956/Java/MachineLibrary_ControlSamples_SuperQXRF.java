





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_ControlSamples_SuperQXRF  {

    private int outOfControl;





    private MachineLibrary_UnitConfig_SuperQ_XRF machinelibrary_unitconfig_superq_xrf;


    public MachineLibrary_ControlSamples_SuperQXRF(
        int outOfControl    ) {
        this.outOfControl = outOfControl;
    }


    public int getOutofcontrol() {
        return outOfControl;
    }

    public void setOutofcontrol(int outOfControl) {
        this.outOfControl = outOfControl;
    }

    public MachineLibrary_UnitConfig_SuperQ_XRF getMachinelibrary_unitconfig_superq_xrf() {
        return machinelibrary_unitconfig_superq_xrf;
    }

    public void setMachinelibrary_unitconfig_superq_xrf(MachineLibrary_UnitConfig_SuperQ_XRF machinelibrary_unitconfig_superq_xrf) {
        this.machinelibrary_unitconfig_superq_xrf = machinelibrary_unitconfig_superq_xrf;
    }

}