





import java.util.List;
import java.util.ArrayList;

public class company106_Action extends NamedElement {

    private String statement;





    private company106_Flow company106_flow;


    public company106_Action(
        String statement    ) {
        super(
        );
        this.statement = statement;
    }


    public String getStatement() {
        return statement;
    }

    public void setStatement(String statement) {
        this.statement = statement;
    }

    public company106_Flow getCompany106_flow() {
        return company106_flow;
    }

    public void setCompany106_flow(company106_Flow company106_flow) {
        this.company106_flow = company106_flow;
    }

}