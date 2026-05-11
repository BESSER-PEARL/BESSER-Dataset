





import java.util.List;
import java.util.ArrayList;

public class gmf_all_mappings_AuditRule extends RuleBase {

    private boolean useInLiveMode;
    private String message;
    private String severity;
    private String id;





    private AuditContainer auditcontainer;


    public gmf_all_mappings_AuditRule(
        boolean useInLiveMode,        String message,        String severity,        String id    ) {
        super(
        );
        this.useInLiveMode = useInLiveMode;
        this.message = message;
        this.severity = severity;
        this.id = id;
    }


    public boolean getUseinlivemode() {
        return useInLiveMode;
    }

    public void setUseinlivemode(boolean useInLiveMode) {
        this.useInLiveMode = useInLiveMode;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public AuditContainer getAuditcontainer() {
        return auditcontainer;
    }

    public void setAuditcontainer(AuditContainer auditcontainer) {
        this.auditcontainer = auditcontainer;
    }

}