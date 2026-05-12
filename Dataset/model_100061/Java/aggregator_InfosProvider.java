





import java.util.List;
import java.util.ArrayList;

public class aggregator_InfosProvider  {

    private String warnings;
    private String errors;
    private String infos;



    public aggregator_InfosProvider(
        String warnings,        String errors,        String infos    ) {
        this.warnings = warnings;
        this.errors = errors;
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
    public String getInfos() {
        return infos;
    }

    public void setInfos(String infos) {
        this.infos = infos;
    }


}