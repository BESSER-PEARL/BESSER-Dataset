





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_SepByComma_ID_Scanner  {

    private int idSeq_X;
    private String idCharValue;
    private String idPrevValue;
    private int idValue;





    private MachineLibrary_SepByComma_Scanner machinelibrary_sepbycomma_scanner;


    public MachineLibrary_SepByComma_ID_Scanner(
        int idSeq_X,        String idCharValue,        String idPrevValue,        int idValue    ) {
        this.idSeq_X = idSeq_X;
        this.idCharValue = idCharValue;
        this.idPrevValue = idPrevValue;
        this.idValue = idValue;
    }


    public int getIdseq_x() {
        return idSeq_X;
    }

    public void setIdseq_x(int idSeq_X) {
        this.idSeq_X = idSeq_X;
    }
    public String getIdcharvalue() {
        return idCharValue;
    }

    public void setIdcharvalue(String idCharValue) {
        this.idCharValue = idCharValue;
    }
    public String getIdprevvalue() {
        return idPrevValue;
    }

    public void setIdprevvalue(String idPrevValue) {
        this.idPrevValue = idPrevValue;
    }
    public int getIdvalue() {
        return idValue;
    }

    public void setIdvalue(int idValue) {
        this.idValue = idValue;
    }

    public MachineLibrary_SepByComma_Scanner getMachinelibrary_sepbycomma_scanner() {
        return machinelibrary_sepbycomma_scanner;
    }

    public void setMachinelibrary_sepbycomma_scanner(MachineLibrary_SepByComma_Scanner machinelibrary_sepbycomma_scanner) {
        this.machinelibrary_sepbycomma_scanner = machinelibrary_sepbycomma_scanner;
    }

}