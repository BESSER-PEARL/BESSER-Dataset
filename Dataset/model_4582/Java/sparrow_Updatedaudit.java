





import java.util.List;
import java.util.ArrayList;

public class sparrow_Updatedaudit extends Action {

    private String logsink;
    private String value;



    public sparrow_Updatedaudit(
        String logsink,        String value    ) {
        super(
        );
        this.logsink = logsink;
        this.value = value;
    }


    public String getLogsink() {
        return logsink;
    }

    public void setLogsink(String logsink) {
        this.logsink = logsink;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}