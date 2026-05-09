





import java.util.List;
import java.util.ArrayList;

public class astm_DataDefinition extends Definition {

    private boolean isMutable;



    public astm_DataDefinition(
        boolean isMutable    ) {
        super(
        );
        this.isMutable = isMutable;
    }


    public boolean getIsmutable() {
        return isMutable;
    }

    public void setIsmutable(boolean isMutable) {
        this.isMutable = isMutable;
    }


}