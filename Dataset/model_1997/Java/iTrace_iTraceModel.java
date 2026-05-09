





import java.util.List;
import java.util.ArrayList;

public class iTrace_iTraceModel  {

    private String version;
    private String projectName;





    private iTrace_Artefact itrace_artefact;




    private iTrace_TraceLink itrace_tracelink;




    private List<iTrace_Artefact> itrace_artefacts;




    private List<iTrace_TraceLink> itrace_tracelinks;


    public iTrace_iTraceModel(
        String version,        String projectName    ) {
        this.version = version;
        this.projectName = projectName;
        this.itrace_artefacts = new ArrayList<>();
        this.itrace_tracelinks = new ArrayList<>();
    }

    public iTrace_iTraceModel(
        String version,        String projectName        ArrayList<iTrace_Artefact> itrace_artefacts,        ArrayList<iTrace_TraceLink> itrace_tracelinks    ) {
        this.version = version;
        this.projectName = projectName;
        this.itrace_artefacts = itrace_artefacts;
        this.itrace_tracelinks = itrace_tracelinks;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getProjectname() {
        return projectName;
    }

    public void setProjectname(String projectName) {
        this.projectName = projectName;
    }

    public iTrace_Artefact getItrace_artefact() {
        return itrace_artefact;
    }

    public void setItrace_artefact(iTrace_Artefact itrace_artefact) {
        this.itrace_artefact = itrace_artefact;
    }
    public iTrace_TraceLink getItrace_tracelink() {
        return itrace_tracelink;
    }

    public void setItrace_tracelink(iTrace_TraceLink itrace_tracelink) {
        this.itrace_tracelink = itrace_tracelink;
    }
    public List<iTrace_Artefact> getItrace_artefacts() {
        return itrace_artefacts;
    }

    public void addItrace_artefact(Itrace_artefact itrace_artefact) {
        this.itrace_artefacts.add(itrace_artefact);
    }
    public List<iTrace_TraceLink> getItrace_tracelinks() {
        return itrace_tracelinks;
    }

    public void addItrace_tracelink(Itrace_tracelink itrace_tracelink) {
        this.itrace_tracelinks.add(itrace_tracelink);
    }

}