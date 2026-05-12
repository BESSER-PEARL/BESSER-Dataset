





import java.util.List;
import java.util.ArrayList;

public class sgraph_Scope  {






    private List<sgraph_Declaration> sgraph_declarations;


    public sgraph_Scope(
    ) {
        this.sgraph_declarations = new ArrayList<>();
    }

    public sgraph_Scope(
        ArrayList<sgraph_Declaration> sgraph_declarations    ) {
        this.sgraph_declarations = sgraph_declarations;
    }


    public List<sgraph_Declaration> getSgraph_declarations() {
        return sgraph_declarations;
    }

    public void addSgraph_declaration(Sgraph_declaration sgraph_declaration) {
        this.sgraph_declarations.add(sgraph_declaration);
    }

}