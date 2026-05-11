





import java.util.List;
import java.util.ArrayList;

public class smartadapters4MODERATES_ScopedInstantiation extends InstantiationStrategy {






    private List<smartadapters4MODERATES_AspectModelElement> smartadapters4moderates_aspectmodelelements;


    public smartadapters4MODERATES_ScopedInstantiation(
    ) {
        super(
        );
        this.smartadapters4moderates_aspectmodelelements = new ArrayList<>();
    }

    public smartadapters4MODERATES_ScopedInstantiation(
        ArrayList<smartadapters4MODERATES_AspectModelElement> smartadapters4moderates_aspectmodelelements    ) {
        this.smartadapters4moderates_aspectmodelelements = smartadapters4moderates_aspectmodelelements;
    }


    public List<smartadapters4MODERATES_AspectModelElement> getSmartadapters4moderates_aspectmodelelements() {
        return smartadapters4moderates_aspectmodelelements;
    }

    public void addSmartadapters4moderates_aspectmodelelement(Smartadapters4moderates_aspectmodelelement smartadapters4moderates_aspectmodelelement) {
        this.smartadapters4moderates_aspectmodelelements.add(smartadapters4moderates_aspectmodelelement);
    }

}