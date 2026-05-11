





import java.util.List;
import java.util.ArrayList;

public class diva_PriorityRule extends Rule {






    private List<diva_PropertyPriority> diva_propertyprioritys;


    public diva_PriorityRule(
    ) {
        super(
        );
        this.diva_propertyprioritys = new ArrayList<>();
    }

    public diva_PriorityRule(
        ArrayList<diva_PropertyPriority> diva_propertyprioritys    ) {
        this.diva_propertyprioritys = diva_propertyprioritys;
    }


    public List<diva_PropertyPriority> getDiva_propertyprioritys() {
        return diva_propertyprioritys;
    }

    public void addDiva_propertypriority(Diva_propertypriority diva_propertypriority) {
        this.diva_propertyprioritys.add(diva_propertypriority);
    }

}