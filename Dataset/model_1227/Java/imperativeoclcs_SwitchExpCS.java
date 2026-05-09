





import java.util.List;
import java.util.ArrayList;

public class imperativeoclcs_SwitchExpCS extends StatementCS {






    private List<imperativeoclcs_SwitchAltCS> imperativeoclcs_switchaltcss;


    public imperativeoclcs_SwitchExpCS(
    ) {
        super(
        );
        this.imperativeoclcs_switchaltcss = new ArrayList<>();
    }

    public imperativeoclcs_SwitchExpCS(
        ArrayList<imperativeoclcs_SwitchAltCS> imperativeoclcs_switchaltcss    ) {
        this.imperativeoclcs_switchaltcss = imperativeoclcs_switchaltcss;
    }


    public List<imperativeoclcs_SwitchAltCS> getImperativeoclcs_switchaltcss() {
        return imperativeoclcs_switchaltcss;
    }

    public void addImperativeoclcs_switchaltcs(Imperativeoclcs_switchaltcs imperativeoclcs_switchaltcs) {
        this.imperativeoclcs_switchaltcss.add(imperativeoclcs_switchaltcs);
    }

}