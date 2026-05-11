





import java.util.List;
import java.util.ArrayList;

public class aggregator_InfosProvider  {

    private String errors;
    private String warnings;
    private String infos;



    public aggregator_InfosProvider(
        String errors,        String warnings,        String infos    ) {
        this.errors = errors;
        this.warnings = warnings;
        this.infos = infos;
    }


    public String getErrors() {
        return errors;
    }

    public void setErrors(String errors) {
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


}