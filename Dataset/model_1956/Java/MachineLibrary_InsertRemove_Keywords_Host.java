





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_InsertRemove_Keywords_Host  {

    private String keywordKey;
    private String keywordValue;





    private MachineLibrary_InsertRemove_Host machinelibrary_insertremove_host;


    public MachineLibrary_InsertRemove_Keywords_Host(
        String keywordKey,        String keywordValue    ) {
        this.keywordKey = keywordKey;
        this.keywordValue = keywordValue;
    }


    public String getKeywordkey() {
        return keywordKey;
    }

    public void setKeywordkey(String keywordKey) {
        this.keywordKey = keywordKey;
    }
    public String getKeywordvalue() {
        return keywordValue;
    }

    public void setKeywordvalue(String keywordValue) {
        this.keywordValue = keywordValue;
    }

    public MachineLibrary_InsertRemove_Host getMachinelibrary_insertremove_host() {
        return machinelibrary_insertremove_host;
    }

    public void setMachinelibrary_insertremove_host(MachineLibrary_InsertRemove_Host machinelibrary_insertremove_host) {
        this.machinelibrary_insertremove_host = machinelibrary_insertremove_host;
    }

}