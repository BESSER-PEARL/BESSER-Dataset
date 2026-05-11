





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_TrgRecTerm extends TrgTerm {

    private String op;





    private List<jointPackage_Ecore2Maude_TrgTerm> jointpackage_ecore2maude_trgterms;


    public jointPackage_Ecore2Maude_TrgRecTerm(
        String op    ) {
        super(
        );
        this.op = op;
        this.jointpackage_ecore2maude_trgterms = new ArrayList<>();
    }

    public jointPackage_Ecore2Maude_TrgRecTerm(
        String op        ArrayList<jointPackage_Ecore2Maude_TrgTerm> jointpackage_ecore2maude_trgterms    ) {
        this.op = op;
        this.jointpackage_ecore2maude_trgterms = jointpackage_ecore2maude_trgterms;
    }

    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public List<jointPackage_Ecore2Maude_TrgTerm> getJointpackage_ecore2maude_trgterms() {
        return jointpackage_ecore2maude_trgterms;
    }

    public void addJointpackage_ecore2maude_trgterm(Jointpackage_ecore2maude_trgterm jointpackage_ecore2maude_trgterm) {
        this.jointpackage_ecore2maude_trgterms.add(jointpackage_ecore2maude_trgterm);
    }

}