





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_TrgInstModExp extends TrgModExpression {






    private List<jointPackage_Ecore2Maude_TrgView> jointpackage_ecore2maude_trgviews;




    private jointPackage_Ecore2Maude_TrgModExpression jointpackage_ecore2maude_trgmodexpression;


    public jointPackage_Ecore2Maude_TrgInstModExp(
    ) {
        super(
        );
        this.jointpackage_ecore2maude_trgviews = new ArrayList<>();
    }

    public jointPackage_Ecore2Maude_TrgInstModExp(
        ArrayList<jointPackage_Ecore2Maude_TrgView> jointpackage_ecore2maude_trgviews    ) {
        this.jointpackage_ecore2maude_trgviews = jointpackage_ecore2maude_trgviews;
    }


    public List<jointPackage_Ecore2Maude_TrgView> getJointpackage_ecore2maude_trgviews() {
        return jointpackage_ecore2maude_trgviews;
    }

    public void addJointpackage_ecore2maude_trgview(Jointpackage_ecore2maude_trgview jointpackage_ecore2maude_trgview) {
        this.jointpackage_ecore2maude_trgviews.add(jointpackage_ecore2maude_trgview);
    }
    public jointPackage_Ecore2Maude_TrgModExpression getJointpackage_ecore2maude_trgmodexpression() {
        return jointpackage_ecore2maude_trgmodexpression;
    }

    public void setJointpackage_ecore2maude_trgmodexpression(jointPackage_Ecore2Maude_TrgModExpression jointpackage_ecore2maude_trgmodexpression) {
        this.jointpackage_ecore2maude_trgmodexpression = jointpackage_ecore2maude_trgmodexpression;
    }

}