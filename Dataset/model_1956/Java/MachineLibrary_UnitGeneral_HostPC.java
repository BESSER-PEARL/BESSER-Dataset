





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_UnitGeneral_HostPC  {

    private int writeDumyIfNoDataExist;
    private int index;
    private int maxIndex;
    private int replyOnLink;





    private MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial;


    public MachineLibrary_UnitGeneral_HostPC(
        int writeDumyIfNoDataExist,        int index,        int maxIndex,        int replyOnLink    ) {
        this.writeDumyIfNoDataExist = writeDumyIfNoDataExist;
        this.index = index;
        this.maxIndex = maxIndex;
        this.replyOnLink = replyOnLink;
    }


    public int getWritedumyifnodataexist() {
        return writeDumyIfNoDataExist;
    }

    public void setWritedumyifnodataexist(int writeDumyIfNoDataExist) {
        this.writeDumyIfNoDataExist = writeDumyIfNoDataExist;
    }
    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }
    public int getMaxindex() {
        return maxIndex;
    }

    public void setMaxindex(int maxIndex) {
        this.maxIndex = maxIndex;
    }
    public int getReplyonlink() {
        return replyOnLink;
    }

    public void setReplyonlink(int replyOnLink) {
        this.replyOnLink = replyOnLink;
    }

    public MachineLibrary_UnitGeneralSpecial getMachinelibrary_unitgeneralspecial() {
        return machinelibrary_unitgeneralspecial;
    }

    public void setMachinelibrary_unitgeneralspecial(MachineLibrary_UnitGeneralSpecial machinelibrary_unitgeneralspecial) {
        this.machinelibrary_unitgeneralspecial = machinelibrary_unitgeneralspecial;
    }

}