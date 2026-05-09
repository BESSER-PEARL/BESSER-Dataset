





import java.util.List;
import java.util.ArrayList;

public class expansionmodel_DiagramExpansion  {

    private String ID;





    private List<expansionmodel_GraphicalElementLibrary> expansionmodel_graphicalelementlibrarys;




    private List<expansionmodel_UseContext> expansionmodel_usecontexts;


    public expansionmodel_DiagramExpansion(
        String ID    ) {
        this.ID = ID;
        this.expansionmodel_graphicalelementlibrarys = new ArrayList<>();
        this.expansionmodel_usecontexts = new ArrayList<>();
    }

    public expansionmodel_DiagramExpansion(
        String ID        ArrayList<expansionmodel_GraphicalElementLibrary> expansionmodel_graphicalelementlibrarys,        ArrayList<expansionmodel_UseContext> expansionmodel_usecontexts    ) {
        this.ID = ID;
        this.expansionmodel_graphicalelementlibrarys = expansionmodel_graphicalelementlibrarys;
        this.expansionmodel_usecontexts = expansionmodel_usecontexts;
    }

    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public List<expansionmodel_GraphicalElementLibrary> getExpansionmodel_graphicalelementlibrarys() {
        return expansionmodel_graphicalelementlibrarys;
    }

    public void addExpansionmodel_graphicalelementlibrary(Expansionmodel_graphicalelementlibrary expansionmodel_graphicalelementlibrary) {
        this.expansionmodel_graphicalelementlibrarys.add(expansionmodel_graphicalelementlibrary);
    }
    public List<expansionmodel_UseContext> getExpansionmodel_usecontexts() {
        return expansionmodel_usecontexts;
    }

    public void addExpansionmodel_usecontext(Expansionmodel_usecontext expansionmodel_usecontext) {
        this.expansionmodel_usecontexts.add(expansionmodel_usecontext);
    }

}