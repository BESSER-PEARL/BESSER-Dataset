





import java.util.List;
import java.util.ArrayList;

public class cloudml_ClientPort extends ArtefactPort {

    private boolean isOptional;



    public cloudml_ClientPort(
        boolean isOptional    ) {
        super(
        );
        this.isOptional = isOptional;
    }


    public boolean getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(boolean isOptional) {
        this.isOptional = isOptional;
    }


}