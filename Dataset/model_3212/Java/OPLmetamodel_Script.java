





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_Script extends Declaration {

    private boolean isMain;



    public OPLmetamodel_Script(
        boolean isMain    ) {
        super(
        );
        this.isMain = isMain;
    }


    public boolean getIsmain() {
        return isMain;
    }

    public void setIsmain(boolean isMain) {
        this.isMain = isMain;
    }


}