





import java.util.List;
import java.util.ArrayList;

public class core_TraceDefinition extends NamedElement {






    private List<core_TraceElement> core_traceelements;




    private core_MatchTrace core_matchtrace;




    private core_PutTrace core_puttrace;




    private core_TraceInterface core_traceinterface;




    private core_TraceUse core_traceuse;


    public core_TraceDefinition(
    ) {
        super(
        );
        this.core_traceelements = new ArrayList<>();
    }

    public core_TraceDefinition(
        ArrayList<core_TraceElement> core_traceelements    ) {
        this.core_traceelements = core_traceelements;
    }


    public List<core_TraceElement> getCore_traceelements() {
        return core_traceelements;
    }

    public void addCore_traceelement(Core_traceelement core_traceelement) {
        this.core_traceelements.add(core_traceelement);
    }
    public core_MatchTrace getCore_matchtrace() {
        return core_matchtrace;
    }

    public void setCore_matchtrace(core_MatchTrace core_matchtrace) {
        this.core_matchtrace = core_matchtrace;
    }
    public core_PutTrace getCore_puttrace() {
        return core_puttrace;
    }

    public void setCore_puttrace(core_PutTrace core_puttrace) {
        this.core_puttrace = core_puttrace;
    }
    public core_TraceInterface getCore_traceinterface() {
        return core_traceinterface;
    }

    public void setCore_traceinterface(core_TraceInterface core_traceinterface) {
        this.core_traceinterface = core_traceinterface;
    }
    public core_TraceUse getCore_traceuse() {
        return core_traceuse;
    }

    public void setCore_traceuse(core_TraceUse core_traceuse) {
        this.core_traceuse = core_traceuse;
    }

}