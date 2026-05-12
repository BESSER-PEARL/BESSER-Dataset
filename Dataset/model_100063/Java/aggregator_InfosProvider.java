





import java.util.List;
import java.util.ArrayList;

public class aggregator_InfosProvider  {

    private String infos;
    private String warnings;
    private String errors;



    public aggregator_InfosProvider(
        String infos,        String warnings,        String errors    ) {
        this.infos = infos;
        this.warnings = warnings;
        this.errors = errors;
    }


    public String getInfos() {
        return infos;
    }

    public void setInfos(String infos) {
        this.infos = infos;
    }
    public String getWarnings() {
        return warnings;
    }

    public void setWarnings(String warnings) {
        this.warnings = warnings;
    }
    public String getErrors() {
        return errors;
    }

    public void setErrors(String errors) {
        this.errors = errors;
    }


}