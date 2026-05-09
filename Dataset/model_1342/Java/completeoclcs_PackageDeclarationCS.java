





import java.util.List;
import java.util.ArrayList;

public class completeoclcs_PackageDeclarationCS extends PathNameDeclCS {






    private List<completeoclcs_ContextDeclCS> completeoclcs_contextdeclcss;




    private completeoclcs_CompleteOCLDocumentCS completeoclcs_completeocldocumentcs;




    private List<completeoclcs_ConstraintCS> completeoclcs_constraintcss;


    public completeoclcs_PackageDeclarationCS(
    ) {
        super(
        );
        this.completeoclcs_contextdeclcss = new ArrayList<>();
        this.completeoclcs_constraintcss = new ArrayList<>();
    }

    public completeoclcs_PackageDeclarationCS(
        ArrayList<completeoclcs_ContextDeclCS> completeoclcs_contextdeclcss,        ArrayList<completeoclcs_ConstraintCS> completeoclcs_constraintcss    ) {
        this.completeoclcs_contextdeclcss = completeoclcs_contextdeclcss;
        this.completeoclcs_constraintcss = completeoclcs_constraintcss;
    }


    public List<completeoclcs_ContextDeclCS> getCompleteoclcs_contextdeclcss() {
        return completeoclcs_contextdeclcss;
    }

    public void addCompleteoclcs_contextdeclcs(Completeoclcs_contextdeclcs completeoclcs_contextdeclcs) {
        this.completeoclcs_contextdeclcss.add(completeoclcs_contextdeclcs);
    }
    public completeoclcs_CompleteOCLDocumentCS getCompleteoclcs_completeocldocumentcs() {
        return completeoclcs_completeocldocumentcs;
    }

    public void setCompleteoclcs_completeocldocumentcs(completeoclcs_CompleteOCLDocumentCS completeoclcs_completeocldocumentcs) {
        this.completeoclcs_completeocldocumentcs = completeoclcs_completeocldocumentcs;
    }
    public List<completeoclcs_ConstraintCS> getCompleteoclcs_constraintcss() {
        return completeoclcs_constraintcss;
    }

    public void addCompleteoclcs_constraintcs(Completeoclcs_constraintcs completeoclcs_constraintcs) {
        this.completeoclcs_constraintcss.add(completeoclcs_constraintcs);
    }

}