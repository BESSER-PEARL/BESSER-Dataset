





import java.util.List;
import java.util.ArrayList;

public class sparql_ANON extends BlankNode {






    private List<sparql_WS> sparql_wss;


    public sparql_ANON(
    ) {
        super(
        );
        this.sparql_wss = new ArrayList<>();
    }

    public sparql_ANON(
        ArrayList<sparql_WS> sparql_wss    ) {
        this.sparql_wss = sparql_wss;
    }


    public List<sparql_WS> getSparql_wss() {
        return sparql_wss;
    }

    public void addSparql_ws(Sparql_ws sparql_ws) {
        this.sparql_wss.add(sparql_ws);
    }

}