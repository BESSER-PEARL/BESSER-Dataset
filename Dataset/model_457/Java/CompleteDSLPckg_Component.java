





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Component extends NamedElement, Class {

    private boolean isIndirectlyInstantiated;



    public CompleteDSLPckg_Component(
        boolean isIndirectlyInstantiated    ) {
        super(
        );
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
    }


    public boolean getIsindirectlyinstantiated() {
        return isIndirectlyInstantiated;
    }

    public void setIsindirectlyinstantiated(boolean isIndirectlyInstantiated) {
        this.isIndirectlyInstantiated = isIndirectlyInstantiated;
    }


}