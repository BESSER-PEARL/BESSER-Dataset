





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_npndiagrams_NPNDiagramNetSystem extends IEntityIdentifiable {






    private List<NPNSymbolArcSN> npnsymbolarcsns;




    private List<NPNSymbolNodeSN> npnsymbolnodesns;


    public highlevelnets_npndiagrams_NPNDiagramNetSystem(
    ) {
        super(
        );
        this.npnsymbolarcsns = new ArrayList<>();
        this.npnsymbolnodesns = new ArrayList<>();
    }

    public highlevelnets_npndiagrams_NPNDiagramNetSystem(
        ArrayList<NPNSymbolArcSN> npnsymbolarcsns,        ArrayList<NPNSymbolNodeSN> npnsymbolnodesns    ) {
        this.npnsymbolarcsns = npnsymbolarcsns;
        this.npnsymbolnodesns = npnsymbolnodesns;
    }


    public List<NPNSymbolArcSN> getNpnsymbolarcsns() {
        return npnsymbolarcsns;
    }

    public void addNpnsymbolarcsn(Npnsymbolarcsn npnsymbolarcsn) {
        this.npnsymbolarcsns.add(npnsymbolarcsn);
    }
    public List<NPNSymbolNodeSN> getNpnsymbolnodesns() {
        return npnsymbolnodesns;
    }

    public void addNpnsymbolnodesn(Npnsymbolnodesn npnsymbolnodesn) {
        this.npnsymbolnodesns.add(npnsymbolnodesn);
    }

}