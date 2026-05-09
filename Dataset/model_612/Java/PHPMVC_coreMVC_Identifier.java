





import java.util.List;
import java.util.ArrayList;

public class PHPMVC_coreMVC_Identifier extends Attribute {

    private boolean isAutoincremental;



    public PHPMVC_coreMVC_Identifier(
        boolean isAutoincremental    ) {
        super(
        );
        this.isAutoincremental = isAutoincremental;
    }


    public boolean getIsautoincremental() {
        return isAutoincremental;
    }

    public void setIsautoincremental(boolean isAutoincremental) {
        this.isAutoincremental = isAutoincremental;
    }


}