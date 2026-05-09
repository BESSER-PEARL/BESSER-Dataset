





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_UnitGeneral_PM2PM  {

    private String sid_Mask;
    private String processFeedBack;





    private MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial;


    public MachineLibrary_UnitGeneral_PM2PM(
        String sid_Mask,        String processFeedBack    ) {
        this.sid_Mask = sid_Mask;
        this.processFeedBack = processFeedBack;
    }


    public String getSid_mask() {
        return sid_Mask;
    }

    public void setSid_mask(String sid_Mask) {
        this.sid_Mask = sid_Mask;
    }
    public String getProcessfeedback() {
        return processFeedBack;
    }

    public void setProcessfeedback(String processFeedBack) {
        this.processFeedBack = processFeedBack;
    }

    public MachineLibrary_UnitGeneralSpecial getMachinelibrary_unitgeneralspecial() {
        return machinelibrary_unitgeneralspecial;
    }

    public void setMachinelibrary_unitgeneralspecial(MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial) {
        this.machinelibrary_unitgeneralspecial = machinelibrary_unitgeneralspecial;
    }

}