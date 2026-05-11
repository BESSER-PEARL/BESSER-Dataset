





import java.util.List;
import java.util.ArrayList;

public class guigraph_GuiGraph extends AbstractModelElement {

    private String invariantText;





    private List<guigraph_Arc> guigraph_arcs;


    public guigraph_GuiGraph(
        String invariantText    ) {
        super(
        );
        this.invariantText = invariantText;
        this.guigraph_arcs = new ArrayList<>();
    }

    public guigraph_GuiGraph(
        String invariantText        ArrayList<guigraph_Arc> guigraph_arcs    ) {
        this.invariantText = invariantText;
        this.guigraph_arcs = guigraph_arcs;
    }

    public String getInvarianttext() {
        return invariantText;
    }

    public void setInvarianttext(String invariantText) {
        this.invariantText = invariantText;
    }

    public List<guigraph_Arc> getGuigraph_arcs() {
        return guigraph_arcs;
    }

    public void addGuigraph_arc(Guigraph_arc guigraph_arc) {
        this.guigraph_arcs.add(guigraph_arc);
    }

}