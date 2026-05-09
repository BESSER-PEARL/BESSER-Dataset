





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_Moved_Host  {

    private int report_ALL;
    private int type0;
    private int pos0;
    private int writePositionNameInFile;





    private MachineLibrary_UnitConfig_Host machinelibrary_unitconfig_host;


    public MachineLibrary_Moved_Host(
        int report_ALL,        int type0,        int pos0,        int writePositionNameInFile    ) {
        this.report_ALL = report_ALL;
        this.type0 = type0;
        this.pos0 = pos0;
        this.writePositionNameInFile = writePositionNameInFile;
    }


    public int getReport_all() {
        return report_ALL;
    }

    public void setReport_all(int report_ALL) {
        this.report_ALL = report_ALL;
    }
    public int getType0() {
        return type0;
    }

    public void setType0(int type0) {
        this.type0 = type0;
    }
    public int getPos0() {
        return pos0;
    }

    public void setPos0(int pos0) {
        this.pos0 = pos0;
    }
    public int getWritepositionnameinfile() {
        return writePositionNameInFile;
    }

    public void setWritepositionnameinfile(int writePositionNameInFile) {
        this.writePositionNameInFile = writePositionNameInFile;
    }

    public MachineLibrary_UnitConfig_Host getMachinelibrary_unitconfig_host() {
        return machinelibrary_unitconfig_host;
    }

    public void setMachinelibrary_unitconfig_host(MachineLibrary_UnitConfig_Host machinelibrary_unitconfig_host) {
        this.machinelibrary_unitconfig_host = machinelibrary_unitconfig_host;
    }

}