





import java.util.List;
import java.util.ArrayList;

public class trace_EMappingOperation  {

    private String module;
    private String name;
    private String package;





    private trace_TraceRecord trace_tracerecord;




    private MappingOperation mappingoperation;


    public trace_EMappingOperation(
        String module,        String name,        String package    ) {
        this.module = module;
        this.name = name;
        this.package = package;
    }


    public String getModule() {
        return module;
    }

    public void setModule(String module) {
        this.module = module;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }

    public trace_TraceRecord getTrace_tracerecord() {
        return trace_tracerecord;
    }

    public void setTrace_tracerecord(trace_TraceRecord trace_tracerecord) {
        this.trace_tracerecord = trace_tracerecord;
    }
    public MappingOperation getMappingoperation() {
        return mappingoperation;
    }

    public void setMappingoperation(MappingOperation mappingoperation) {
        this.mappingoperation = mappingoperation;
    }

}