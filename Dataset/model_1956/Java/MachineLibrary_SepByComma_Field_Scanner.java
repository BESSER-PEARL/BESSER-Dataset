





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_SepByComma_Field_Scanner  {

    private int fieldNo;
    private String fieldName;





    private MachineLibrary_SepByComma_Scanner machinelibrary_sepbycomma_scanner;


    public MachineLibrary_SepByComma_Field_Scanner(
        int fieldNo,        String fieldName    ) {
        this.fieldNo = fieldNo;
        this.fieldName = fieldName;
    }


    public int getFieldno() {
        return fieldNo;
    }

    public void setFieldno(int fieldNo) {
        this.fieldNo = fieldNo;
    }
    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }

    public MachineLibrary_SepByComma_Scanner getMachinelibrary_sepbycomma_scanner() {
        return machinelibrary_sepbycomma_scanner;
    }

    public void setMachinelibrary_sepbycomma_scanner(MachineLibrary_SepByComma_Scanner machinelibrary_sepbycomma_scanner) {
        this.machinelibrary_sepbycomma_scanner = machinelibrary_sepbycomma_scanner;
    }

}