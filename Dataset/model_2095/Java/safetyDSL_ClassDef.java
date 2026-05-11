





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_ClassDef  {

    private String name;





    private safetyDSL_ModuleClassRelation safetydsl_moduleclassrelation;




    private safetyDSL_ClassTestCaseRelation safetydsl_classtestcaserelation;


    public safetyDSL_ClassDef(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public safetyDSL_ModuleClassRelation getSafetydsl_moduleclassrelation() {
        return safetydsl_moduleclassrelation;
    }

    public void setSafetydsl_moduleclassrelation(safetyDSL_ModuleClassRelation safetydsl_moduleclassrelation) {
        this.safetydsl_moduleclassrelation = safetydsl_moduleclassrelation;
    }
    public safetyDSL_ClassTestCaseRelation getSafetydsl_classtestcaserelation() {
        return safetydsl_classtestcaserelation;
    }

    public void setSafetydsl_classtestcaserelation(safetyDSL_ClassTestCaseRelation safetydsl_classtestcaserelation) {
        this.safetydsl_classtestcaserelation = safetydsl_classtestcaserelation;
    }

}