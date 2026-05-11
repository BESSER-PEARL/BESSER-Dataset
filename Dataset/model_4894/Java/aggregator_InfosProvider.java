





import java.util.List;
import java.util.ArrayList;

public class aggregator_InfosProvider  {

    private String warnings;
    private String infos;
    private String errors;



    public aggregator_InfosProvider(
        String warnings,        String infos,        String errors    ) {
        this.warnings = warnings;
        this.infos = infos;
        this.errors = errors;
    }


    public String getWarnings() {
        return warnings;
    }

    public void setWarnings(String warnings) {
        this.warnings = warnings;
    }
    public String getInfos() {
        return infos;
    }

    public void setInfos(String infos) {
        this.infos = infos;
    }
    public String getErrors() {
        return errors;
    }

    public void setErrors(String errors) {
        this.errors = errors;
    }


}