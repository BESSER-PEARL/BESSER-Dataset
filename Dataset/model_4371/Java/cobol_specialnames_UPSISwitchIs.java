





import java.util.List;
import java.util.ArrayList;

public class cobol_specialnames_UPSISwitchIs extends specialnames_MnemonicName, specialnames_SpecialNameStatement {






    private List<ConditionName> conditionnames;


    public cobol_specialnames_UPSISwitchIs(
    ) {
        super(
        );
        this.conditionnames = new ArrayList<>();
    }

    public cobol_specialnames_UPSISwitchIs(
        ArrayList<ConditionName> conditionnames    ) {
        this.conditionnames = conditionnames;
    }


    public List<ConditionName> getConditionnames() {
        return conditionnames;
    }

    public void addConditionname(Conditionname conditionname) {
        this.conditionnames.add(conditionname);
    }

}