





import java.util.List;
import java.util.ArrayList;

public class uma_ContentDescription extends MethodUnit {

    private String keyConsiderations;
    private String mainDescription;



    public uma_ContentDescription(
        String keyConsiderations,        String mainDescription    ) {
        super(
        );
        this.keyConsiderations = keyConsiderations;
        this.mainDescription = mainDescription;
    }


    public String getKeyconsiderations() {
        return keyConsiderations;
    }

    public void setKeyconsiderations(String keyConsiderations) {
        this.keyConsiderations = keyConsiderations;
    }
    public String getMaindescription() {
        return mainDescription;
    }

    public void setMaindescription(String mainDescription) {
        this.mainDescription = mainDescription;
    }


}