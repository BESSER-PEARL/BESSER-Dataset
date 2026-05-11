





import java.util.List;
import java.util.ArrayList;

public class company106_Function extends NamedElement {






    private company106_Flow company106_flow;




    private List<company106_Flow> company106_flows;




    private company106_Flow company106_flow;


    public company106_Function(
    ) {
        super(
        );
        this.company106_flows = new ArrayList<>();
    }

    public company106_Function(
        ArrayList<company106_Flow> company106_flows    ) {
        this.company106_flows = company106_flows;
    }


    public company106_Flow getCompany106_flow() {
        return company106_flow;
    }

    public void setCompany106_flow(company106_Flow company106_flow) {
        this.company106_flow = company106_flow;
    }
    public List<company106_Flow> getCompany106_flows() {
        return company106_flows;
    }

    public void addCompany106_flow(Company106_flow company106_flow) {
        this.company106_flows.add(company106_flow);
    }
    public company106_Flow getCompany106_flow() {
        return company106_flow;
    }

    public void setCompany106_flow(company106_Flow company106_flow) {
        this.company106_flow = company106_flow;
    }

}