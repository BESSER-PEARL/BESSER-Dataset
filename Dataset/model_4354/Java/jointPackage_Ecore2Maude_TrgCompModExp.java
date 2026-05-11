





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_TrgCompModExp extends TrgModExpression {






    private List<jointPackage_Ecore2Maude_TrgModExpression> jointpackage_ecore2maude_trgmodexpressions;


    public jointPackage_Ecore2Maude_TrgCompModExp(
    ) {
        super(
        );
        this.jointpackage_ecore2maude_trgmodexpressions = new ArrayList<>();
    }

    public jointPackage_Ecore2Maude_TrgCompModExp(
        ArrayList<jointPackage_Ecore2Maude_TrgModExpression> jointpackage_ecore2maude_trgmodexpressions    ) {
        this.jointpackage_ecore2maude_trgmodexpressions = jointpackage_ecore2maude_trgmodexpressions;
    }


    public List<jointPackage_Ecore2Maude_TrgModExpression> getJointpackage_ecore2maude_trgmodexpressions() {
        return jointpackage_ecore2maude_trgmodexpressions;
    }

    public void addJointpackage_ecore2maude_trgmodexpression(Jointpackage_ecore2maude_trgmodexpression jointpackage_ecore2maude_trgmodexpression) {
        this.jointpackage_ecore2maude_trgmodexpressions.add(jointpackage_ecore2maude_trgmodexpression);
    }

}