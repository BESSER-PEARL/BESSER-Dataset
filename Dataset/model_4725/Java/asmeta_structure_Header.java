





import java.util.List;
import java.util.ArrayList;

public class asmeta_structure_Header  {






    private List<ImportClause> importclauses;




    private Asm asm;




    private Signature signature;




    private ExportClause exportclause;


    public asmeta_structure_Header(
    ) {
        this.importclauses = new ArrayList<>();
    }

    public asmeta_structure_Header(
        ArrayList<ImportClause> importclauses    ) {
        this.importclauses = importclauses;
    }


    public List<ImportClause> getImportclauses() {
        return importclauses;
    }

    public void addImportclause(Importclause importclause) {
        this.importclauses.add(importclause);
    }
    public Asm getAsm() {
        return asm;
    }

    public void setAsm(Asm asm) {
        this.asm = asm;
    }
    public Signature getSignature() {
        return signature;
    }

    public void setSignature(Signature signature) {
        this.signature = signature;
    }
    public ExportClause getExportclause() {
        return exportclause;
    }

    public void setExportclause(ExportClause exportclause) {
        this.exportclause = exportclause;
    }

}