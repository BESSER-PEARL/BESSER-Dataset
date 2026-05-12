





import java.util.List;
import java.util.ArrayList;

public class aggregator_InfosProvider  {

    private String infos;
    private String errors;
    private String warnings;



    public aggregator_InfosProvider(
        String infos,        String errors,        String warnings    ) {
        this.infos = infos;
        this.errors = errors;
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
    public String getWarnings() {
        return warnings;
    }

    public void setWarnings(String warnings) {
        this.warnings = warnings;
    }


}