





import java.util.List;
import java.util.ArrayList;

public class express_core_LocalScope extends Scope {






    private List<LocalElement> localelements;


    public express_core_LocalScope(
    ) {
        super(
        );
        this.localelements = new ArrayList<>();
    }

    public express_core_LocalScope(
        ArrayList<LocalElement> localelements    ) {
        this.localelements = localelements;
    }


    public List<LocalElement> getLocalelements() {
        return localelements;
    }

    public void addLocalelement(Localelement localelement) {
        this.localelements.add(localelement);
    }

}