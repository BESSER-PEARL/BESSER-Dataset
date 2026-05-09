





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_Communication_SuperQXRF  {

    private int enq_ACK_Protocol;





    private MachineLibrary_UnitConfig_SuperQ_XRF machinelibrary_unitconfig_superq_xrf;


    public MachineLibrary_Communication_SuperQXRF(
        int enq_ACK_Protocol    ) {
        this.enq_ACK_Protocol = enq_ACK_Protocol;
    }


    public int getEnq_ack_protocol() {
        return enq_ACK_Protocol;
    }

    public void setEnq_ack_protocol(int enq_ACK_Protocol) {
        this.enq_ACK_Protocol = enq_ACK_Protocol;
    }

    public MachineLibrary_UnitConfig_SuperQ_XRF getMachinelibrary_unitconfig_superq_xrf() {
        return machinelibrary_unitconfig_superq_xrf;
    }

    public void setMachinelibrary_unitconfig_superq_xrf(MachineLibrary_UnitConfig_SuperQ_XRF machinelibrary_unitconfig_superq_xrf) {
        this.machinelibrary_unitconfig_superq_xrf = machinelibrary_unitconfig_superq_xrf;
    }

}