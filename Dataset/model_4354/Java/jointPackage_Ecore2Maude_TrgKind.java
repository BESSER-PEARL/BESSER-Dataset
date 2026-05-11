





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_TrgKind extends TrgType {






    private jointPackage_Ecore2Maude_TrgSort jointpackage_ecore2maude_trgsort;




    private List<jointPackage_Ecore2Maude_TrgSort> jointpackage_ecore2maude_trgsorts;


    public jointPackage_Ecore2Maude_TrgKind(
    ) {
        super(
        );
        this.jointpackage_ecore2maude_trgsorts = new ArrayList<>();
    }

    public jointPackage_Ecore2Maude_TrgKind(
        ArrayList<jointPackage_Ecore2Maude_TrgSort> jointpackage_ecore2maude_trgsorts    ) {
        this.jointpackage_ecore2maude_trgsorts = jointpackage_ecore2maude_trgsorts;
    }


    public jointPackage_Ecore2Maude_TrgSort getJointpackage_ecore2maude_trgsort() {
        return jointpackage_ecore2maude_trgsort;
    }

    public void setJointpackage_ecore2maude_trgsort(jointPackage_Ecore2Maude_TrgSort jointpackage_ecore2maude_trgsort) {
        this.jointpackage_ecore2maude_trgsort = jointpackage_ecore2maude_trgsort;
    }
    public List<jointPackage_Ecore2Maude_TrgSort> getJointpackage_ecore2maude_trgsorts() {
        return jointpackage_ecore2maude_trgsorts;
    }

    public void addJointpackage_ecore2maude_trgsort(Jointpackage_ecore2maude_trgsort jointpackage_ecore2maude_trgsort) {
        this.jointpackage_ecore2maude_trgsorts.add(jointpackage_ecore2maude_trgsort);
    }

}