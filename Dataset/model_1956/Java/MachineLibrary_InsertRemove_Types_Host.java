





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_InsertRemove_Types_Host  {

    private String typeValue;
    private int typeNo;





    private MachineLibrary_InsertRemove_Host machinelibrary_insertremove_host;


    public MachineLibrary_InsertRemove_Types_Host(
        String typeValue,        int typeNo    ) {
        this.typeValue = typeValue;
        this.typeNo = typeNo;
    }


    public String getTypevalue() {
        return typeValue;
    }

    public void setTypevalue(String typeValue) {
        this.typeValue = typeValue;
    }
    public int getTypeno() {
        return typeNo;
    }

    public void setTypeno(int typeNo) {
        this.typeNo = typeNo;
    }

    public MachineLibrary_InsertRemove_Host getMachinelibrary_insertremove_host() {
        return machinelibrary_insertremove_host;
    }

    public void setMachinelibrary_insertremove_host(MachineLibrary_InsertRemove_Host machinelibrary_insertremove_host) {
        this.machinelibrary_insertremove_host = machinelibrary_insertremove_host;
    }

}