





import java.util.List;
import java.util.ArrayList;

public class diagraph_DGraph  {

    private String facade2;
    private String facade1;
    private String viewName;





    private diagraph_DGraphElement diagraph_dgraphelement;




    private List<diagraph_DGraphElement> diagraph_dgraphelements;


    public diagraph_DGraph(
        String facade2,        String facade1,        String viewName    ) {
        this.facade2 = facade2;
        this.facade1 = facade1;
        this.viewName = viewName;
        this.diagraph_dgraphelements = new ArrayList<>();
    }

    public diagraph_DGraph(
        String facade2,        String facade1,        String viewName        ArrayList<diagraph_DGraphElement> diagraph_dgraphelements    ) {
        this.facade2 = facade2;
        this.facade1 = facade1;
        this.viewName = viewName;
        this.diagraph_dgraphelements = diagraph_dgraphelements;
    }

    public String getFacade2() {
        return facade2;
    }

    public void setFacade2(String facade2) {
        this.facade2 = facade2;
    }
    public String getFacade1() {
        return facade1;
    }

    public void setFacade1(String facade1) {
        this.facade1 = facade1;
    }
    public String getViewname() {
        return viewName;
    }

    public void setViewname(String viewName) {
        this.viewName = viewName;
    }

    public diagraph_DGraphElement getDiagraph_dgraphelement() {
        return diagraph_dgraphelement;
    }

    public void setDiagraph_dgraphelement(diagraph_DGraphElement diagraph_dgraphelement) {
        this.diagraph_dgraphelement = diagraph_dgraphelement;
    }
    public List<diagraph_DGraphElement> getDiagraph_dgraphelements() {
        return diagraph_dgraphelements;
    }

    public void addDiagraph_dgraphelement(Diagraph_dgraphelement diagraph_dgraphelement) {
        this.diagraph_dgraphelements.add(diagraph_dgraphelement);
    }

}