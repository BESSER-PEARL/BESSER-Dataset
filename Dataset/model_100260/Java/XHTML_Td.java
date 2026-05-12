





import java.util.List;
import java.util.ArrayList;

public class XHTML_Td extends Cellhalign, Cellvalign, TrElement, Attrs {

    private String scope;





    private Text text;




    private CDATA cdata;




    private Number number;




    private Number number;




    private List<Flow> flows;


    public XHTML_Td(
        String scope    ) {
        super(
        );
        this.scope = scope;
        this.flows = new ArrayList<>();
    }

    public XHTML_Td(
        String scope        ArrayList<Flow> flows    ) {
        this.scope = scope;
        this.flows = flows;
    }

    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }

    public Text getText() {
        return text;
    }

    public void setText(Text text) {
        this.text = text;
    }
    public CDATA getCdata() {
        return cdata;
    }

    public void setCdata(CDATA cdata) {
        this.cdata = cdata;
    }
    public Number getNumber() {
        return number;
    }

    public void setNumber(Number number) {
        this.number = number;
    }
    public Number getNumber() {
        return number;
    }

    public void setNumber(Number number) {
        this.number = number;
    }
    public List<Flow> getFlows() {
        return flows;
    }

    public void addFlow(Flow flow) {
        this.flows.add(flow);
    }

}