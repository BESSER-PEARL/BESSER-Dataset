





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_InsertRemove_Entry_Host  {

    private int entryNo;
    private String entryName;





    private MachineLibrary_InsertRemove_Host machinelibrary_insertremove_host;


    public MachineLibrary_InsertRemove_Entry_Host(
        int entryNo,        String entryName    ) {
        this.entryNo = entryNo;
        this.entryName = entryName;
    }


    public int getEntryno() {
        return entryNo;
    }

    public void setEntryno(int entryNo) {
        this.entryNo = entryNo;
    }
    public String getEntryname() {
        return entryName;
    }

    public void setEntryname(String entryName) {
        this.entryName = entryName;
    }

    public MachineLibrary_InsertRemove_Host getMachinelibrary_insertremove_host() {
        return machinelibrary_insertremove_host;
    }

    public void setMachinelibrary_insertremove_host(MachineLibrary_InsertRemove_Host machinelibrary_insertremove_host) {
        this.machinelibrary_insertremove_host = machinelibrary_insertremove_host;
    }

}