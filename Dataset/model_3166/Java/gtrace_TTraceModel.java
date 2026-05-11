





import java.util.List;
import java.util.ArrayList;

public class gtrace_TTraceModel  {

    private String name;





    private List<gtrace_TScenarioStepTrace> gtrace_tscenariosteptraces;


    public gtrace_TTraceModel(
        String name    ) {
        this.name = name;
        this.gtrace_tscenariosteptraces = new ArrayList<>();
    }

    public gtrace_TTraceModel(
        String name        ArrayList<gtrace_TScenarioStepTrace> gtrace_tscenariosteptraces    ) {
        this.name = name;
        this.gtrace_tscenariosteptraces = gtrace_tscenariosteptraces;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<gtrace_TScenarioStepTrace> getGtrace_tscenariosteptraces() {
        return gtrace_tscenariosteptraces;
    }

    public void addGtrace_tscenariosteptrace(Gtrace_tscenariosteptrace gtrace_tscenariosteptrace) {
        this.gtrace_tscenariosteptraces.add(gtrace_tscenariosteptrace);
    }

}