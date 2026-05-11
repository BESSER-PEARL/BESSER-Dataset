





import java.util.List;
import java.util.ArrayList;

public class carnot_PoolSymbol extends ISymbolContainer, ISwimlaneSymbol {

    private String boundaryVisible;





    private carnot_DiagramType carnot_diagramtype;




    private List<carnot_LaneSymbol> carnot_lanesymbols;




    private carnot_ProcessDefinitionType carnot_processdefinitiontype;




    private carnot_DiagramType carnot_diagramtype;




    private carnot_LaneSymbol carnot_lanesymbol;


    public carnot_PoolSymbol(
        String boundaryVisible    ) {
        super(
        );
        this.boundaryVisible = boundaryVisible;
        this.carnot_lanesymbols = new ArrayList<>();
    }

    public carnot_PoolSymbol(
        String boundaryVisible        ArrayList<carnot_LaneSymbol> carnot_lanesymbols    ) {
        this.boundaryVisible = boundaryVisible;
        this.carnot_lanesymbols = carnot_lanesymbols;
    }

    public String getBoundaryvisible() {
        return boundaryVisible;
    }

    public void setBoundaryvisible(String boundaryVisible) {
        this.boundaryVisible = boundaryVisible;
    }

    public carnot_DiagramType getCarnot_diagramtype() {
        return carnot_diagramtype;
    }

    public void setCarnot_diagramtype(carnot_DiagramType carnot_diagramtype) {
        this.carnot_diagramtype = carnot_diagramtype;
    }
    public List<carnot_LaneSymbol> getCarnot_lanesymbols() {
        return carnot_lanesymbols;
    }

    public void addCarnot_lanesymbol(Carnot_lanesymbol carnot_lanesymbol) {
        this.carnot_lanesymbols.add(carnot_lanesymbol);
    }
    public carnot_ProcessDefinitionType getCarnot_processdefinitiontype() {
        return carnot_processdefinitiontype;
    }

    public void setCarnot_processdefinitiontype(carnot_ProcessDefinitionType carnot_processdefinitiontype) {
        this.carnot_processdefinitiontype = carnot_processdefinitiontype;
    }
    public carnot_DiagramType getCarnot_diagramtype() {
        return carnot_diagramtype;
    }

    public void setCarnot_diagramtype(carnot_DiagramType carnot_diagramtype) {
        this.carnot_diagramtype = carnot_diagramtype;
    }
    public carnot_LaneSymbol getCarnot_lanesymbol() {
        return carnot_lanesymbol;
    }

    public void setCarnot_lanesymbol(carnot_LaneSymbol carnot_lanesymbol) {
        this.carnot_lanesymbol = carnot_lanesymbol;
    }

}