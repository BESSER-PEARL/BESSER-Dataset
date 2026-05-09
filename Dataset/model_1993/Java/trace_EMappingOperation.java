





import java.util.List;
import java.util.ArrayList;

public class trace_EMappingOperation  {

    private String package;
    private String name;
    private String module;





    private trace_TraceRecord trace_tracerecord;


    public trace_EMappingOperation(
        String package,        String name,        String module    ) {
        this.package = package;
        this.name = name;
        this.module = module;
    }


    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getModule() {
        return module;
    }

    public void setModule(String module) {
        this.module = module;
    }

    public trace_TraceRecord getTrace_tracerecord() {
        return trace_tracerecord;
    }

    public void setTrace_tracerecord(trace_TraceRecord trace_tracerecord) {
        this.trace_tracerecord = trace_tracerecord;
    }

}