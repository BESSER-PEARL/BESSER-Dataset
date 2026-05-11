





import java.util.List;
import java.util.ArrayList;

public class adb_DiscreteChoiceList  {






    private adb_Variant adb_variant;




    private adb_CaseStatementAlternative adb_casestatementalternative;




    private List<adb_DiscreteChoice> adb_discretechoices;




    private adb_ArrayComponentAssociation adb_arraycomponentassociation;


    public adb_DiscreteChoiceList(
    ) {
        this.adb_discretechoices = new ArrayList<>();
    }

    public adb_DiscreteChoiceList(
        ArrayList<adb_DiscreteChoice> adb_discretechoices    ) {
        this.adb_discretechoices = adb_discretechoices;
    }


    public adb_Variant getAdb_variant() {
        return adb_variant;
    }

    public void setAdb_variant(adb_Variant adb_variant) {
        this.adb_variant = adb_variant;
    }
    public adb_CaseStatementAlternative getAdb_casestatementalternative() {
        return adb_casestatementalternative;
    }

    public void setAdb_casestatementalternative(adb_CaseStatementAlternative adb_casestatementalternative) {
        this.adb_casestatementalternative = adb_casestatementalternative;
    }
    public List<adb_DiscreteChoice> getAdb_discretechoices() {
        return adb_discretechoices;
    }

    public void addAdb_discretechoice(Adb_discretechoice adb_discretechoice) {
        this.adb_discretechoices.add(adb_discretechoice);
    }
    public adb_ArrayComponentAssociation getAdb_arraycomponentassociation() {
        return adb_arraycomponentassociation;
    }

    public void setAdb_arraycomponentassociation(adb_ArrayComponentAssociation adb_arraycomponentassociation) {
        this.adb_arraycomponentassociation = adb_arraycomponentassociation;
    }

}