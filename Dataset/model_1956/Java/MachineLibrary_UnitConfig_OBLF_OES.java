





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_UnitConfig_OBLF_OES  {






    private List<MachineLibrary_RecalRequest_OBLFOES> machinelibrary_recalrequest_oblfoess;




    private MachineLibrary_ErrorMessage_OBLFOES machinelibrary_errormessage_oblfoes;




    private MachineLibrary_OutputRequest_OBLFOES machinelibrary_outputrequest_oblfoes;




    private List<MachineLibrary_TestRequest_OBLFOES> machinelibrary_testrequest_oblfoess;




    private MachineLibrary_UnitSpecialConfiguration machinelibrary_unitspecialconfiguration;


    public MachineLibrary_UnitConfig_OBLF_OES(
    ) {
        this.machinelibrary_recalrequest_oblfoess = new ArrayList<>();
        this.machinelibrary_testrequest_oblfoess = new ArrayList<>();
    }

    public MachineLibrary_UnitConfig_OBLF_OES(
        ArrayList<MachineLibrary_RecalRequest_OBLFOES> machinelibrary_recalrequest_oblfoess,        ArrayList<MachineLibrary_TestRequest_OBLFOES> machinelibrary_testrequest_oblfoess    ) {
        this.machinelibrary_recalrequest_oblfoess = machinelibrary_recalrequest_oblfoess;
        this.machinelibrary_testrequest_oblfoess = machinelibrary_testrequest_oblfoess;
    }


    public List<MachineLibrary_RecalRequest_OBLFOES> getMachinelibrary_recalrequest_oblfoess() {
        return machinelibrary_recalrequest_oblfoess;
    }

    public void addMachinelibrary_recalrequest_oblfoes(Machinelibrary_recalrequest_oblfoes machinelibrary_recalrequest_oblfoes) {
        this.machinelibrary_recalrequest_oblfoess.add(machinelibrary_recalrequest_oblfoes);
    }
    public MachineLibrary_ErrorMessage_OBLFOES getMachinelibrary_errormessage_oblfoes() {
        return machinelibrary_errormessage_oblfoes;
    }

    public void setMachinelibrary_errormessage_oblfoes(MachineLibrary_ErrorMessage_OBLFOES machinelibrary_errormessage_oblfoes) {
        this.machinelibrary_errormessage_oblfoes = machinelibrary_errormessage_oblfoes;
    }
    public MachineLibrary_OutputRequest_OBLFOES getMachinelibrary_outputrequest_oblfoes() {
        return machinelibrary_outputrequest_oblfoes;
    }

    public void setMachinelibrary_outputrequest_oblfoes(MachineLibrary_OutputRequest_OBLFOES machinelibrary_outputrequest_oblfoes) {
        this.machinelibrary_outputrequest_oblfoes = machinelibrary_outputrequest_oblfoes;
    }
    public List<MachineLibrary_TestRequest_OBLFOES> getMachinelibrary_testrequest_oblfoess() {
        return machinelibrary_testrequest_oblfoess;
    }

    public void addMachinelibrary_testrequest_oblfoes(Machinelibrary_testrequest_oblfoes machinelibrary_testrequest_oblfoes) {
        this.machinelibrary_testrequest_oblfoess.add(machinelibrary_testrequest_oblfoes);
    }
    public MachineLibrary_UnitSpecialConfiguration getMachinelibrary_unitspecialconfiguration() {
        return machinelibrary_unitspecialconfiguration;
    }

    public void setMachinelibrary_unitspecialconfiguration(MachineLibrary_UnitSpecialConfiguration machinelibrary_unitspecialconfiguration) {
        this.machinelibrary_unitspecialconfiguration = machinelibrary_unitspecialconfiguration;
    }

}