





import java.util.List;
import java.util.ArrayList;

public class siddhi_ExecutionPlan  {






    private List<siddhi_DefinitionTable> siddhi_definitiontables;




    private List<siddhi_DefinitionStream> siddhi_definitionstreams;




    private List<siddhi_DefinitionAggregation> siddhi_definitionaggregations;




    private List<siddhi_DefinitionWindow> siddhi_definitionwindows;




    private List<siddhi_ExecutionElement> siddhi_executionelements;




    private siddhi_SiddhiQL siddhi_siddhiql;




    private List<siddhi_DefinitionFunction> siddhi_definitionfunctions;




    private List<siddhi_DefinitionTrigger> siddhi_definitiontriggers;


    public siddhi_ExecutionPlan(
    ) {
        this.siddhi_definitiontables = new ArrayList<>();
        this.siddhi_definitionstreams = new ArrayList<>();
        this.siddhi_definitionaggregations = new ArrayList<>();
        this.siddhi_definitionwindows = new ArrayList<>();
        this.siddhi_executionelements = new ArrayList<>();
        this.siddhi_definitionfunctions = new ArrayList<>();
        this.siddhi_definitiontriggers = new ArrayList<>();
    }

    public siddhi_ExecutionPlan(
        ArrayList<siddhi_DefinitionTable> siddhi_definitiontables,        ArrayList<siddhi_DefinitionStream> siddhi_definitionstreams,        ArrayList<siddhi_DefinitionAggregation> siddhi_definitionaggregations,        ArrayList<siddhi_DefinitionWindow> siddhi_definitionwindows,        ArrayList<siddhi_ExecutionElement> siddhi_executionelements,        ArrayList<siddhi_DefinitionFunction> siddhi_definitionfunctions,        ArrayList<siddhi_DefinitionTrigger> siddhi_definitiontriggers    ) {
        this.siddhi_definitiontables = siddhi_definitiontables;
        this.siddhi_definitionstreams = siddhi_definitionstreams;
        this.siddhi_definitionaggregations = siddhi_definitionaggregations;
        this.siddhi_definitionwindows = siddhi_definitionwindows;
        this.siddhi_executionelements = siddhi_executionelements;
        this.siddhi_definitionfunctions = siddhi_definitionfunctions;
        this.siddhi_definitiontriggers = siddhi_definitiontriggers;
    }


    public List<siddhi_DefinitionTable> getSiddhi_definitiontables() {
        return siddhi_definitiontables;
    }

    public void addSiddhi_definitiontable(Siddhi_definitiontable siddhi_definitiontable) {
        this.siddhi_definitiontables.add(siddhi_definitiontable);
    }
    public List<siddhi_DefinitionStream> getSiddhi_definitionstreams() {
        return siddhi_definitionstreams;
    }

    public void addSiddhi_definitionstream(Siddhi_definitionstream siddhi_definitionstream) {
        this.siddhi_definitionstreams.add(siddhi_definitionstream);
    }
    public List<siddhi_DefinitionAggregation> getSiddhi_definitionaggregations() {
        return siddhi_definitionaggregations;
    }

    public void addSiddhi_definitionaggregation(Siddhi_definitionaggregation siddhi_definitionaggregation) {
        this.siddhi_definitionaggregations.add(siddhi_definitionaggregation);
    }
    public List<siddhi_DefinitionWindow> getSiddhi_definitionwindows() {
        return siddhi_definitionwindows;
    }

    public void addSiddhi_definitionwindow(Siddhi_definitionwindow siddhi_definitionwindow) {
        this.siddhi_definitionwindows.add(siddhi_definitionwindow);
    }
    public List<siddhi_ExecutionElement> getSiddhi_executionelements() {
        return siddhi_executionelements;
    }

    public void addSiddhi_executionelement(Siddhi_executionelement siddhi_executionelement) {
        this.siddhi_executionelements.add(siddhi_executionelement);
    }
    public siddhi_SiddhiQL getSiddhi_siddhiql() {
        return siddhi_siddhiql;
    }

    public void setSiddhi_siddhiql(siddhi_SiddhiQL siddhi_siddhiql) {
        this.siddhi_siddhiql = siddhi_siddhiql;
    }
    public List<siddhi_DefinitionFunction> getSiddhi_definitionfunctions() {
        return siddhi_definitionfunctions;
    }

    public void addSiddhi_definitionfunction(Siddhi_definitionfunction siddhi_definitionfunction) {
        this.siddhi_definitionfunctions.add(siddhi_definitionfunction);
    }
    public List<siddhi_DefinitionTrigger> getSiddhi_definitiontriggers() {
        return siddhi_definitiontriggers;
    }

    public void addSiddhi_definitiontrigger(Siddhi_definitiontrigger siddhi_definitiontrigger) {
        this.siddhi_definitiontriggers.add(siddhi_definitiontrigger);
    }

}