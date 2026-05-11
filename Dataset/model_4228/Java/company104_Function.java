





import java.util.List;
import java.util.ArrayList;

public class company104_Function extends NamedElement {






    private List<company104_Flow> company104_flows;




    private company104_Flow company104_flow;




    private company104_Flow company104_flow;


    public company104_Function(
    ) {
        super(
        );
        this.company104_flows = new ArrayList<>();
    }

    public company104_Function(
        ArrayList<company104_Flow> company104_flows    ) {
        this.company104_flows = company104_flows;
    }


    public List<company104_Flow> getCompany104_flows() {
        return company104_flows;
    }

    public void addCompany104_flow(Company104_flow company104_flow) {
        this.company104_flows.add(company104_flow);
    }
    public company104_Flow getCompany104_flow() {
        return company104_flow;
    }

    public void setCompany104_flow(company104_Flow company104_flow) {
        this.company104_flow = company104_flow;
    }
    public company104_Flow getCompany104_flow() {
        return company104_flow;
    }

    public void setCompany104_flow(company104_Flow company104_flow) {
        this.company104_flow = company104_flow;
    }

}