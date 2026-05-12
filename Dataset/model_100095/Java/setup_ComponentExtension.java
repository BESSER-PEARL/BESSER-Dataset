





import java.util.List;
import java.util.ArrayList;

public class setup_ComponentExtension  {






    private List<setup_InstallableUnit> setup_installableunits;


    public setup_ComponentExtension(
    ) {
        this.setup_installableunits = new ArrayList<>();
    }

    public setup_ComponentExtension(
        ArrayList<setup_InstallableUnit> setup_installableunits    ) {
        this.setup_installableunits = setup_installableunits;
    }


    public List<setup_InstallableUnit> getSetup_installableunits() {
        return setup_installableunits;
    }

    public void addSetup_installableunit(Setup_installableunit setup_installableunit) {
        this.setup_installableunits.add(setup_installableunit);
    }

}