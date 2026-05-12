





import java.util.List;
import java.util.ArrayList;

public class connection_Query extends AbstractMetadataObject {

    private boolean contextMode;
    private String value;



    public connection_Query(
        boolean contextMode,        String value    ) {
        super(
        );
        this.contextMode = contextMode;
        this.value = value;
    }


    public boolean getContextmode() {
        return contextMode;
    }

    public void setContextmode(boolean contextMode) {
        this.contextMode = contextMode;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}