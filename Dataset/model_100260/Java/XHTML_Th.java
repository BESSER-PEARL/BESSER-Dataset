





import java.util.List;
import java.util.ArrayList;

public class XHTML_Th extends Cellhalign, Cellvalign, TrElement, Attrs {

    private String scope;





    private Number number;




    private Number number;




    private CDATA cdata;




    private Text text;




    private List<Flow> flows;


    public XHTML_Th(
        String scope    ) {
        super(
        );
        this.scope = scope;
        this.flows = new ArrayList<>();
    }

    public XHTML_Th(
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
    public CDATA getCdata() {
        return cdata;
    }

    public void setCdata(CDATA cdata) {
        this.cdata = cdata;
    }
    public Text getText() {
        return text;
    }

    public void setText(Text text) {
        this.text = text;
    }
    public List<Flow> getFlows() {
        return flows;
    }

    public void addFlow(Flow flow) {
        this.flows.add(flow);
    }

}