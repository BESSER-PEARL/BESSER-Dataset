





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_SrcEEnum extends SrcEDataType {






    private jointPackage_Ecore2Maude_SrcEEnumLiteral jointpackage_ecore2maude_srceenumliteral;




    private List<jointPackage_Ecore2Maude_SrcEEnumLiteral> jointpackage_ecore2maude_srceenumliterals;


    public jointPackage_Ecore2Maude_SrcEEnum(
    ) {
        super(
        );
        this.jointpackage_ecore2maude_srceenumliterals = new ArrayList<>();
    }

    public jointPackage_Ecore2Maude_SrcEEnum(
        ArrayList<jointPackage_Ecore2Maude_SrcEEnumLiteral> jointpackage_ecore2maude_srceenumliterals    ) {
        this.jointpackage_ecore2maude_srceenumliterals = jointpackage_ecore2maude_srceenumliterals;
    }


    public jointPackage_Ecore2Maude_SrcEEnumLiteral getJointpackage_ecore2maude_srceenumliteral() {
        return jointpackage_ecore2maude_srceenumliteral;
    }

    public void setJointpackage_ecore2maude_srceenumliteral(jointPackage_Ecore2Maude_SrcEEnumLiteral jointpackage_ecore2maude_srceenumliteral) {
        this.jointpackage_ecore2maude_srceenumliteral = jointpackage_ecore2maude_srceenumliteral;
    }
    public List<jointPackage_Ecore2Maude_SrcEEnumLiteral> getJointpackage_ecore2maude_srceenumliterals() {
        return jointpackage_ecore2maude_srceenumliterals;
    }

    public void addJointpackage_ecore2maude_srceenumliteral(Jointpackage_ecore2maude_srceenumliteral jointpackage_ecore2maude_srceenumliteral) {
        this.jointpackage_ecore2maude_srceenumliterals.add(jointpackage_ecore2maude_srceenumliteral);
    }

}