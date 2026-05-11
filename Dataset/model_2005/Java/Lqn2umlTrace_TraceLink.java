





import java.util.List;
import java.util.ArrayList;

public class Lqn2umlTrace_TraceLink  {

    private String description;
    private String sources;
    private String targets;





    private Lqn2umlTrace_Trace lqn2umltrace_trace;


    public Lqn2umlTrace_TraceLink(
        String description,        String sources,        String targets    ) {
        this.description = description;
        this.sources = sources;
        this.targets = targets;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getSources() {
        return sources;
    }

    public void setSources(String sources) {
        this.sources = sources;
    }
    public String getTargets() {
        return targets;
    }

    public void setTargets(String targets) {
        this.targets = targets;
    }

    public Lqn2umlTrace_Trace getLqn2umltrace_trace() {
        return lqn2umltrace_trace;
    }

    public void setLqn2umltrace_trace(Lqn2umlTrace_Trace lqn2umltrace_trace) {
        this.lqn2umltrace_trace = lqn2umltrace_trace;
    }

}