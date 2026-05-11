





import java.util.List;
import java.util.ArrayList;

public class build_IClosure extends PropertyScope, IPrerequisites {

    private boolean executeOnce;



    public build_IClosure(
        boolean executeOnce    ) {
        super(
        );
        this.executeOnce = executeOnce;
    }


    public boolean getExecuteonce() {
        return executeOnce;
    }

    public void setExecuteonce(boolean executeOnce) {
        this.executeOnce = executeOnce;
    }


}