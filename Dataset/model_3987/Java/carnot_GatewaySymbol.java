





import java.util.List;
import java.util.ArrayList;

public class carnot_GatewaySymbol extends IFlowObjectSymbol {

    private String flowKind;





    private carnot_ISymbolContainer carnot_isymbolcontainer;


    public carnot_GatewaySymbol(
        String flowKind    ) {
        super(
        );
        this.flowKind = flowKind;
    }


    public String getFlowkind() {
        return flowKind;
    }

    public void setFlowkind(String flowKind) {
        this.flowKind = flowKind;
    }

    public carnot_ISymbolContainer getCarnot_isymbolcontainer() {
        return carnot_isymbolcontainer;
    }

    public void setCarnot_isymbolcontainer(carnot_ISymbolContainer carnot_isymbolcontainer) {
        this.carnot_isymbolcontainer = carnot_isymbolcontainer;
    }

}