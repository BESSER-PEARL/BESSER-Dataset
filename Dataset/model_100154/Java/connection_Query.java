





import java.util.List;
import java.util.ArrayList;

public class connection_Query extends AbstractMetadataObject {

    private String value;
    private boolean contextMode;



    public connection_Query(
        String value,        boolean contextMode    ) {
        super(
        );
        this.value = value;
        this.contextMode = contextMode;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getContextmode() {
        return contextMode;
    }

    public void setContextmode(boolean contextMode) {
        this.contextMode = contextMode;
    }


}