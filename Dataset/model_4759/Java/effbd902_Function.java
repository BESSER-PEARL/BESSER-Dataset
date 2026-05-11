





import java.util.List;
import java.util.ArrayList;

public class effbd902_Function extends AbstractFunction, SequenceNode, ProcessNode {

    private String domain;





    private List<effbd902_Description> effbd902_descriptions;


    public effbd902_Function(
        String domain    ) {
        super(
        );
        this.domain = domain;
        this.effbd902_descriptions = new ArrayList<>();
    }

    public effbd902_Function(
        String domain        ArrayList<effbd902_Description> effbd902_descriptions    ) {
        this.domain = domain;
        this.effbd902_descriptions = effbd902_descriptions;
    }

    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }

    public List<effbd902_Description> getEffbd902_descriptions() {
        return effbd902_descriptions;
    }

    public void addEffbd902_description(Effbd902_description effbd902_description) {
        this.effbd902_descriptions.add(effbd902_description);
    }

}