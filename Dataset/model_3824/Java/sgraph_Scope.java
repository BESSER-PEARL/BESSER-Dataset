





import java.util.List;
import java.util.ArrayList;

public class sgraph_Scope  {






    private List<sgraph_Reaction> sgraph_reactions;


    public sgraph_Scope(
    ) {
        this.sgraph_reactions = new ArrayList<>();
    }

    public sgraph_Scope(
        ArrayList<sgraph_Reaction> sgraph_reactions    ) {
        this.sgraph_reactions = sgraph_reactions;
    }


    public List<sgraph_Reaction> getSgraph_reactions() {
        return sgraph_reactions;
    }

    public void addSgraph_reaction(Sgraph_reaction sgraph_reaction) {
        this.sgraph_reactions.add(sgraph_reaction);
    }

}