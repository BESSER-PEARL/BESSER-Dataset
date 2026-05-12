





import java.util.List;
import java.util.ArrayList;

public class sgraph_Scope  {






    private List<sgraph_Event> sgraph_events;




    private List<sgraph_Variable> sgraph_variables;




    private List<sgraph_Declaration> sgraph_declarations;


    public sgraph_Scope(
    ) {
        this.sgraph_events = new ArrayList<>();
        this.sgraph_variables = new ArrayList<>();
        this.sgraph_declarations = new ArrayList<>();
    }

    public sgraph_Scope(
        ArrayList<sgraph_Event> sgraph_events,        ArrayList<sgraph_Variable> sgraph_variables,        ArrayList<sgraph_Declaration> sgraph_declarations    ) {
        this.sgraph_events = sgraph_events;
        this.sgraph_variables = sgraph_variables;
        this.sgraph_declarations = sgraph_declarations;
    }


    public List<sgraph_Event> getSgraph_events() {
        return sgraph_events;
    }

    public void addSgraph_event(Sgraph_event sgraph_event) {
        this.sgraph_events.add(sgraph_event);
    }
    public List<sgraph_Variable> getSgraph_variables() {
        return sgraph_variables;
    }

    public void addSgraph_variable(Sgraph_variable sgraph_variable) {
        this.sgraph_variables.add(sgraph_variable);
    }
    public List<sgraph_Declaration> getSgraph_declarations() {
        return sgraph_declarations;
    }

    public void addSgraph_declaration(Sgraph_declaration sgraph_declaration) {
        this.sgraph_declarations.add(sgraph_declaration);
    }

}