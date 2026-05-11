





import java.util.List;
import java.util.ArrayList;

public class website_UnitSupportAction extends NamedDisplayElement {

    private String confirmMessage;
    private boolean disable;



    public website_UnitSupportAction(
        String confirmMessage,        boolean disable    ) {
        super(
        );
        this.confirmMessage = confirmMessage;
        this.disable = disable;
    }


    public String getConfirmmessage() {
        return confirmMessage;
    }

    public void setConfirmmessage(String confirmMessage) {
        this.confirmMessage = confirmMessage;
    }
    public boolean getDisable() {
        return disable;
    }

    public void setDisable(boolean disable) {
        this.disable = disable;
    }


}