





import java.util.List;
import java.util.ArrayList;

public class activity_ActivityPartition extends AbstractNamedElement, ModelElement {

    private boolean isExternal;
    private boolean isDimension;



    public activity_ActivityPartition(
        boolean isExternal,        boolean isDimension    ) {
        super(
        );
        this.isExternal = isExternal;
        this.isDimension = isDimension;
    }


    public boolean getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(boolean isExternal) {
        this.isExternal = isExternal;
    }
    public boolean getIsdimension() {
        return isDimension;
    }

    public void setIsdimension(boolean isDimension) {
        this.isDimension = isDimension;
    }


}