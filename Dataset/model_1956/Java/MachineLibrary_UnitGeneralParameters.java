





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_UnitGeneralParameters  {

    private String paraName_1;
    private int minValue_1;
    private int defaultValue_1;
    private String UseWith_1;
    private int canBeChange_1;
    private String unit_1;
    private int seq_X;
    private String comment_1;
    private int maxValue_1;
    private int visibleType_1;
    private String KeyWord_1;





    private MachineLibrary_UnitGeneral machinelibrary_unitgeneral;


    public MachineLibrary_UnitGeneralParameters(
        String paraName_1,        int minValue_1,        int defaultValue_1,        String UseWith_1,        int canBeChange_1,        String unit_1,        int seq_X,        String comment_1,        int maxValue_1,        int visibleType_1,        String KeyWord_1    ) {
        this.paraName_1 = paraName_1;
        this.minValue_1 = minValue_1;
        this.defaultValue_1 = defaultValue_1;
        this.UseWith_1 = UseWith_1;
        this.canBeChange_1 = canBeChange_1;
        this.unit_1 = unit_1;
        this.seq_X = seq_X;
        this.comment_1 = comment_1;
        this.maxValue_1 = maxValue_1;
        this.visibleType_1 = visibleType_1;
        this.KeyWord_1 = KeyWord_1;
    }


    public String getParaname_1() {
        return paraName_1;
    }

    public void setParaname_1(String paraName_1) {
        this.paraName_1 = paraName_1;
    }
    public int getMinvalue_1() {
        return minValue_1;
    }

    public void setMinvalue_1(int minValue_1) {
        this.minValue_1 = minValue_1;
    }
    public int getDefaultvalue_1() {
        return defaultValue_1;
    }

    public void setDefaultvalue_1(int defaultValue_1) {
        this.defaultValue_1 = defaultValue_1;
    }
    public String getUsewith_1() {
        return UseWith_1;
    }

    public void setUsewith_1(String UseWith_1) {
        this.UseWith_1 = UseWith_1;
    }
    public int getCanbechange_1() {
        return canBeChange_1;
    }

    public void setCanbechange_1(int canBeChange_1) {
        this.canBeChange_1 = canBeChange_1;
    }
    public String getUnit_1() {
        return unit_1;
    }

    public void setUnit_1(String unit_1) {
        this.unit_1 = unit_1;
    }
    public int getSeq_x() {
        return seq_X;
    }

    public void setSeq_x(int seq_X) {
        this.seq_X = seq_X;
    }
    public String getComment_1() {
        return comment_1;
    }

    public void setComment_1(String comment_1) {
        this.comment_1 = comment_1;
    }
    public int getMaxvalue_1() {
        return maxValue_1;
    }

    public void setMaxvalue_1(int maxValue_1) {
        this.maxValue_1 = maxValue_1;
    }
    public int getVisibletype_1() {
        return visibleType_1;
    }

    public void setVisibletype_1(int visibleType_1) {
        this.visibleType_1 = visibleType_1;
    }
    public String getKeyword_1() {
        return KeyWord_1;
    }

    public void setKeyword_1(String KeyWord_1) {
        this.KeyWord_1 = KeyWord_1;
    }

    public MachineLibrary_UnitGeneral getMachinelibrary_unitgeneral() {
        return machinelibrary_unitgeneral;
    }

    public void setMachinelibrary_unitgeneral(MachineLibrary_UnitGeneral machinelibrary_unitgeneral) {
        this.machinelibrary_unitgeneral = machinelibrary_unitgeneral;
    }

}