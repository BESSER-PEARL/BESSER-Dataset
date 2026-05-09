





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_OES_XRF_Condition  {

    private String paraName;
    private String para;
    private int seq_X;
    private String comment;





    private MachineLibrary_ExecuteFiling_ARL_XRF_OES machinelibrary_executefiling_arl_xrf_oes;




    private MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES machinelibrary_checkaskprepunit_arl_xrf_oes;




    private MachineLibrary_OutputRequest_OBLFOES machinelibrary_outputrequest_oblfoes;




    private MachineLibrary_ExePrepUnit_ARL_XRF_OES machinelibrary_exeprepunit_arl_xrf_oes;




    private MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES machinelibrary_exeaskprepunit_arl_xrf_oes;




    private MachineLibrary_Settings_ARL_XRF_OES machinelibrary_settings_arl_xrf_oes;




    private MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES machinelibrary_checkreqprepunit_arl_xrf_oes;




    private MachineLibrary_GeneralSetting_ARL_XRF_OES machinelibrary_generalsetting_arl_xrf_oes;




    private MachineLibrary_DisableSCT_ARL_XRF_OES machinelibrary_disablesct_arl_xrf_oes;




    private MachineLibrary_RecalRequest_OBLFOES machinelibrary_recalrequest_oblfoes;




    private MachineLibrary_CheckFilling_ARL_XRF_OES machinelibrary_checkfilling_arl_xrf_oes;




    private MachineLibrary_TestRequest_OBLFOES machinelibrary_testrequest_oblfoes;


    public MachineLibrary_OES_XRF_Condition(
        String paraName,        String para,        int seq_X,        String comment    ) {
        this.paraName = paraName;
        this.para = para;
        this.seq_X = seq_X;
        this.comment = comment;
    }


    public String getParaname() {
        return paraName;
    }

    public void setParaname(String paraName) {
        this.paraName = paraName;
    }
    public String getPara() {
        return para;
    }

    public void setPara(String para) {
        this.para = para;
    }
    public int getSeq_x() {
        return seq_X;
    }

    public void setSeq_x(int seq_X) {
        this.seq_X = seq_X;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public MachineLibrary_ExecuteFiling_ARL_XRF_OES getMachinelibrary_executefiling_arl_xrf_oes() {
        return machinelibrary_executefiling_arl_xrf_oes;
    }

    public void setMachinelibrary_executefiling_arl_xrf_oes(MachineLibrary_ExecuteFiling_ARL_XRF_OES machinelibrary_executefiling_arl_xrf_oes) {
        this.machinelibrary_executefiling_arl_xrf_oes = machinelibrary_executefiling_arl_xrf_oes;
    }
    public MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES getMachinelibrary_checkaskprepunit_arl_xrf_oes() {
        return machinelibrary_checkaskprepunit_arl_xrf_oes;
    }

    public void setMachinelibrary_checkaskprepunit_arl_xrf_oes(MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES machinelibrary_checkaskprepunit_arl_xrf_oes) {
        this.machinelibrary_checkaskprepunit_arl_xrf_oes = machinelibrary_checkaskprepunit_arl_xrf_oes;
    }
    public MachineLibrary_OutputRequest_OBLFOES getMachinelibrary_outputrequest_oblfoes() {
        return machinelibrary_outputrequest_oblfoes;
    }

    public void setMachinelibrary_outputrequest_oblfoes(MachineLibrary_OutputRequest_OBLFOES machinelibrary_outputrequest_oblfoes) {
        this.machinelibrary_outputrequest_oblfoes = machinelibrary_outputrequest_oblfoes;
    }
    public MachineLibrary_ExePrepUnit_ARL_XRF_OES getMachinelibrary_exeprepunit_arl_xrf_oes() {
        return machinelibrary_exeprepunit_arl_xrf_oes;
    }

    public void setMachinelibrary_exeprepunit_arl_xrf_oes(MachineLibrary_ExePrepUnit_ARL_XRF_OES machinelibrary_exeprepunit_arl_xrf_oes) {
        this.machinelibrary_exeprepunit_arl_xrf_oes = machinelibrary_exeprepunit_arl_xrf_oes;
    }
    public MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES getMachinelibrary_exeaskprepunit_arl_xrf_oes() {
        return machinelibrary_exeaskprepunit_arl_xrf_oes;
    }

    public void setMachinelibrary_exeaskprepunit_arl_xrf_oes(MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES machinelibrary_exeaskprepunit_arl_xrf_oes) {
        this.machinelibrary_exeaskprepunit_arl_xrf_oes = machinelibrary_exeaskprepunit_arl_xrf_oes;
    }
    public MachineLibrary_Settings_ARL_XRF_OES getMachinelibrary_settings_arl_xrf_oes() {
        return machinelibrary_settings_arl_xrf_oes;
    }

    public void setMachinelibrary_settings_arl_xrf_oes(MachineLibrary_Settings_ARL_XRF_OES machinelibrary_settings_arl_xrf_oes) {
        this.machinelibrary_settings_arl_xrf_oes = machinelibrary_settings_arl_xrf_oes;
    }
    public MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES getMachinelibrary_checkreqprepunit_arl_xrf_oes() {
        return machinelibrary_checkreqprepunit_arl_xrf_oes;
    }

    public void setMachinelibrary_checkreqprepunit_arl_xrf_oes(MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES machinelibrary_checkreqprepunit_arl_xrf_oes) {
        this.machinelibrary_checkreqprepunit_arl_xrf_oes = machinelibrary_checkreqprepunit_arl_xrf_oes;
    }
    public MachineLibrary_GeneralSetting_ARL_XRF_OES getMachinelibrary_generalsetting_arl_xrf_oes() {
        return machinelibrary_generalsetting_arl_xrf_oes;
    }

    public void setMachinelibrary_generalsetting_arl_xrf_oes(MachineLibrary_GeneralSetting_ARL_XRF_OES machinelibrary_generalsetting_arl_xrf_oes) {
        this.machinelibrary_generalsetting_arl_xrf_oes = machinelibrary_generalsetting_arl_xrf_oes;
    }
    public MachineLibrary_DisableSCT_ARL_XRF_OES getMachinelibrary_disablesct_arl_xrf_oes() {
        return machinelibrary_disablesct_arl_xrf_oes;
    }

    public void setMachinelibrary_disablesct_arl_xrf_oes(MachineLibrary_DisableSCT_ARL_XRF_OES machinelibrary_disablesct_arl_xrf_oes) {
        this.machinelibrary_disablesct_arl_xrf_oes = machinelibrary_disablesct_arl_xrf_oes;
    }
    public MachineLibrary_RecalRequest_OBLFOES getMachinelibrary_recalrequest_oblfoes() {
        return machinelibrary_recalrequest_oblfoes;
    }

    public void setMachinelibrary_recalrequest_oblfoes(MachineLibrary_RecalRequest_OBLFOES machinelibrary_recalrequest_oblfoes) {
        this.machinelibrary_recalrequest_oblfoes = machinelibrary_recalrequest_oblfoes;
    }
    public MachineLibrary_CheckFilling_ARL_XRF_OES getMachinelibrary_checkfilling_arl_xrf_oes() {
        return machinelibrary_checkfilling_arl_xrf_oes;
    }

    public void setMachinelibrary_checkfilling_arl_xrf_oes(MachineLibrary_CheckFilling_ARL_XRF_OES machinelibrary_checkfilling_arl_xrf_oes) {
        this.machinelibrary_checkfilling_arl_xrf_oes = machinelibrary_checkfilling_arl_xrf_oes;
    }
    public MachineLibrary_TestRequest_OBLFOES getMachinelibrary_testrequest_oblfoes() {
        return machinelibrary_testrequest_oblfoes;
    }

    public void setMachinelibrary_testrequest_oblfoes(MachineLibrary_TestRequest_OBLFOES machinelibrary_testrequest_oblfoes) {
        this.machinelibrary_testrequest_oblfoes = machinelibrary_testrequest_oblfoes;
    }

}