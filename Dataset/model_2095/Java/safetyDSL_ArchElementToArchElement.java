





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_ArchElementToArchElement extends SafetyCriticalRelation {






    private List<safetyDSL_ArchitecturalElement> safetydsl_architecturalelements;




    private safetyDSL_ArchitecturalElement safetydsl_architecturalelement;


    public safetyDSL_ArchElementToArchElement(
    ) {
        super(
        );
        this.safetydsl_architecturalelements = new ArrayList<>();
    }

    public safetyDSL_ArchElementToArchElement(
        ArrayList<safetyDSL_ArchitecturalElement> safetydsl_architecturalelements    ) {
        this.safetydsl_architecturalelements = safetydsl_architecturalelements;
    }


    public List<safetyDSL_ArchitecturalElement> getSafetydsl_architecturalelements() {
        return safetydsl_architecturalelements;
    }

    public void addSafetydsl_architecturalelement(Safetydsl_architecturalelement safetydsl_architecturalelement) {
        this.safetydsl_architecturalelements.add(safetydsl_architecturalelement);
    }
    public safetyDSL_ArchitecturalElement getSafetydsl_architecturalelement() {
        return safetydsl_architecturalelement;
    }

    public void setSafetydsl_architecturalelement(safetyDSL_ArchitecturalElement safetydsl_architecturalelement) {
        this.safetydsl_architecturalelement = safetydsl_architecturalelement;
    }

}