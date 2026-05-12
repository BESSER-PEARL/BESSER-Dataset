





import java.util.List;
import java.util.ArrayList;

public class sgraph_Reaction  {






    private List<sgraph_ReactionProperty> sgraph_reactionpropertys;




    private sgraph_ReactiveElement sgraph_reactiveelement;




    private sgraph_ReactiveElement sgraph_reactiveelement;


    public sgraph_Reaction(
    ) {
        this.sgraph_reactionpropertys = new ArrayList<>();
    }

    public sgraph_Reaction(
        ArrayList<sgraph_ReactionProperty> sgraph_reactionpropertys    ) {
        this.sgraph_reactionpropertys = sgraph_reactionpropertys;
    }


    public List<sgraph_ReactionProperty> getSgraph_reactionpropertys() {
        return sgraph_reactionpropertys;
    }

    public void addSgraph_reactionproperty(Sgraph_reactionproperty sgraph_reactionproperty) {
        this.sgraph_reactionpropertys.add(sgraph_reactionproperty);
    }
    public sgraph_ReactiveElement getSgraph_reactiveelement() {
        return sgraph_reactiveelement;
    }

    public void setSgraph_reactiveelement(sgraph_ReactiveElement sgraph_reactiveelement) {
        this.sgraph_reactiveelement = sgraph_reactiveelement;
    }
    public sgraph_ReactiveElement getSgraph_reactiveelement() {
        return sgraph_reactiveelement;
    }

    public void setSgraph_reactiveelement(sgraph_ReactiveElement sgraph_reactiveelement) {
        this.sgraph_reactiveelement = sgraph_reactiveelement;
    }

}