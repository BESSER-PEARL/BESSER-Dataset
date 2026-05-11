





import java.util.List;
import java.util.ArrayList;

public class guigraph_GuiGraph extends AbstractModelElement {

    private String invariantText;





    private guigraph_PageTransition guigraph_pagetransition;




    private Predicate predicate;




    private List<guigraph_Arc> guigraph_arcs;




    private List<guigraph_GuiGraphNode> guigraph_guigraphnodes;


    public guigraph_GuiGraph(
        String invariantText    ) {
        super(
        );
        this.invariantText = invariantText;
        this.guigraph_arcs = new ArrayList<>();
        this.guigraph_guigraphnodes = new ArrayList<>();
    }

    public guigraph_GuiGraph(
        String invariantText        ArrayList<guigraph_Arc> guigraph_arcs,        ArrayList<guigraph_GuiGraphNode> guigraph_guigraphnodes    ) {
        this.invariantText = invariantText;
        this.guigraph_arcs = guigraph_arcs;
        this.guigraph_guigraphnodes = guigraph_guigraphnodes;
    }

    public String getInvarianttext() {
        return invariantText;
    }

    public void setInvarianttext(String invariantText) {
        this.invariantText = invariantText;
    }

    public guigraph_PageTransition getGuigraph_pagetransition() {
        return guigraph_pagetransition;
    }

    public void setGuigraph_pagetransition(guigraph_PageTransition guigraph_pagetransition) {
        this.guigraph_pagetransition = guigraph_pagetransition;
    }
    public Predicate getPredicate() {
        return predicate;
    }

    public void setPredicate(Predicate predicate) {
        this.predicate = predicate;
    }
    public List<guigraph_Arc> getGuigraph_arcs() {
        return guigraph_arcs;
    }

    public void addGuigraph_arc(Guigraph_arc guigraph_arc) {
        this.guigraph_arcs.add(guigraph_arc);
    }
    public List<guigraph_GuiGraphNode> getGuigraph_guigraphnodes() {
        return guigraph_guigraphnodes;
    }

    public void addGuigraph_guigraphnode(Guigraph_guigraphnode guigraph_guigraphnode) {
        this.guigraph_guigraphnodes.add(guigraph_guigraphnode);
    }

}