





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_TrgModule extends TrgMaudeTopEl {






    private jointPackage_Ecore2Maude_TrgModuleIdModExp jointpackage_ecore2maude_trgmoduleidmodexp;




    private List<jointPackage_Ecore2Maude_TrgParameter> jointpackage_ecore2maude_trgparameters;


    public jointPackage_Ecore2Maude_TrgModule(
    ) {
        super(
        );
        this.jointpackage_ecore2maude_trgparameters = new ArrayList<>();
    }

    public jointPackage_Ecore2Maude_TrgModule(
        ArrayList<jointPackage_Ecore2Maude_TrgParameter> jointpackage_ecore2maude_trgparameters    ) {
        this.jointpackage_ecore2maude_trgparameters = jointpackage_ecore2maude_trgparameters;
    }


    public jointPackage_Ecore2Maude_TrgModuleIdModExp getJointpackage_ecore2maude_trgmoduleidmodexp() {
        return jointpackage_ecore2maude_trgmoduleidmodexp;
    }

    public void setJointpackage_ecore2maude_trgmoduleidmodexp(jointPackage_Ecore2Maude_TrgModuleIdModExp jointpackage_ecore2maude_trgmoduleidmodexp) {
        this.jointpackage_ecore2maude_trgmoduleidmodexp = jointpackage_ecore2maude_trgmoduleidmodexp;
    }
    public List<jointPackage_Ecore2Maude_TrgParameter> getJointpackage_ecore2maude_trgparameters() {
        return jointpackage_ecore2maude_trgparameters;
    }

    public void addJointpackage_ecore2maude_trgparameter(Jointpackage_ecore2maude_trgparameter jointpackage_ecore2maude_trgparameter) {
        this.jointpackage_ecore2maude_trgparameters.add(jointpackage_ecore2maude_trgparameter);
    }

}