





import java.util.List;
import java.util.ArrayList;

public class iTrace_Artefact  {

    private String aspect;
    private String path;
    private String name;
    private String abstractionLevel;





    private iTrace_iTraceModel itrace_itracemodel;




    private iTrace_iTraceModel itrace_itracemodel;


    public iTrace_Artefact(
        String aspect,        String path,        String name,        String abstractionLevel    ) {
        this.aspect = aspect;
        this.path = path;
        this.name = name;
        this.abstractionLevel = abstractionLevel;
    }


    public String getAspect() {
        return aspect;
    }

    public void setAspect(String aspect) {
        this.aspect = aspect;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAbstractionlevel() {
        return abstractionLevel;
    }

    public void setAbstractionlevel(String abstractionLevel) {
        this.abstractionLevel = abstractionLevel;
    }

    public iTrace_iTraceModel getItrace_itracemodel() {
        return itrace_itracemodel;
    }

    public void setItrace_itracemodel(iTrace_iTraceModel itrace_itracemodel) {
        this.itrace_itracemodel = itrace_itracemodel;
    }
    public iTrace_iTraceModel getItrace_itracemodel() {
        return itrace_itracemodel;
    }

    public void setItrace_itracemodel(iTrace_iTraceModel itrace_itracemodel) {
        this.itrace_itracemodel = itrace_itracemodel;
    }

}