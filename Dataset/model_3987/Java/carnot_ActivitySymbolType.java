





import java.util.List;
import java.util.ArrayList;

public class carnot_ActivitySymbolType extends IFlowObjectSymbol, IModelElementNodeSymbol {






    private carnot_ActivityType carnot_activitytype;




    private carnot_ISymbolContainer carnot_isymbolcontainer;




    private List<carnot_GatewaySymbol> carnot_gatewaysymbols;




    private carnot_GatewaySymbol carnot_gatewaysymbol;




    private carnot_ActivityType carnot_activitytype;


    public carnot_ActivitySymbolType(
    ) {
        super(
        );
        this.carnot_gatewaysymbols = new ArrayList<>();
    }

    public carnot_ActivitySymbolType(
        ArrayList<carnot_GatewaySymbol> carnot_gatewaysymbols    ) {
        this.carnot_gatewaysymbols = carnot_gatewaysymbols;
    }


    public carnot_ActivityType getCarnot_activitytype() {
        return carnot_activitytype;
    }

    public void setCarnot_activitytype(carnot_ActivityType carnot_activitytype) {
        this.carnot_activitytype = carnot_activitytype;
    }
    public carnot_ISymbolContainer getCarnot_isymbolcontainer() {
        return carnot_isymbolcontainer;
    }

    public void setCarnot_isymbolcontainer(carnot_ISymbolContainer carnot_isymbolcontainer) {
        this.carnot_isymbolcontainer = carnot_isymbolcontainer;
    }
    public List<carnot_GatewaySymbol> getCarnot_gatewaysymbols() {
        return carnot_gatewaysymbols;
    }

    public void addCarnot_gatewaysymbol(Carnot_gatewaysymbol carnot_gatewaysymbol) {
        this.carnot_gatewaysymbols.add(carnot_gatewaysymbol);
    }
    public carnot_GatewaySymbol getCarnot_gatewaysymbol() {
        return carnot_gatewaysymbol;
    }

    public void setCarnot_gatewaysymbol(carnot_GatewaySymbol carnot_gatewaysymbol) {
        this.carnot_gatewaysymbol = carnot_gatewaysymbol;
    }
    public carnot_ActivityType getCarnot_activitytype() {
        return carnot_activitytype;
    }

    public void setCarnot_activitytype(carnot_ActivityType carnot_activitytype) {
        this.carnot_activitytype = carnot_activitytype;
    }

}