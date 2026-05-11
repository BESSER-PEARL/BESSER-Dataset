





import java.util.List;
import java.util.ArrayList;

public class Lqn2umlTrace_TraceLink  {

    private String sources;
    private String description;
    private String targets;





    private Lqn2umlTrace_Trace lqn2umltrace_trace;


    public Lqn2umlTrace_TraceLink(
        String sources,        String description,        String targets    ) {
        this.sources = sources;
        this.description = description;
        this.targets = targets;
    }


    public String getSources() {
        return sources;
    }

    public void setSources(String sources) {
        this.sources = sources;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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