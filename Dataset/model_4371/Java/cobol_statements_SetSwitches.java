





import java.util.List;
import java.util.ArrayList;

public class cobol_statements_SetSwitches extends SetStatement {






    private List<SwitchStatus> switchstatuss;


    public cobol_statements_SetSwitches(
    ) {
        super(
        );
        this.switchstatuss = new ArrayList<>();
    }

    public cobol_statements_SetSwitches(
        ArrayList<SwitchStatus> switchstatuss    ) {
        this.switchstatuss = switchstatuss;
    }


    public List<SwitchStatus> getSwitchstatuss() {
        return switchstatuss;
    }

    public void addSwitchstatus(Switchstatus switchstatus) {
        this.switchstatuss.add(switchstatus);
    }

}