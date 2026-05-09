





import java.util.List;
import java.util.ArrayList;

public class trace_VarParameterValue  {

    private String name;
    private String type;
    private String kind;





    private trace_EMappingResults trace_emappingresults;




    private trace_EMappingParameters trace_emappingparameters;


    public trace_VarParameterValue(
        String name,        String type,        String kind    ) {
        this.name = name;
        this.type = type;
        this.kind = kind;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public trace_EMappingResults getTrace_emappingresults() {
        return trace_emappingresults;
    }

    public void setTrace_emappingresults(trace_EMappingResults trace_emappingresults) {
        this.trace_emappingresults = trace_emappingresults;
    }
    public trace_EMappingParameters getTrace_emappingparameters() {
        return trace_emappingparameters;
    }

    public void setTrace_emappingparameters(trace_EMappingParameters trace_emappingparameters) {
        this.trace_emappingparameters = trace_emappingparameters;
    }

}