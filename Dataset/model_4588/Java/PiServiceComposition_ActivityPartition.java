





import java.util.List;
import java.util.ArrayList;

public class PiServiceComposition_ActivityPartition extends NamedElement {

    private boolean isDimension;
    private boolean isExternal;





    private PiServiceComposition_CompositionServiceModel piservicecomposition_compositionservicemodel;




    private PiServiceComposition_ActivityPartition piservicecomposition_activitypartition;


    public PiServiceComposition_ActivityPartition(
        boolean isDimension,        boolean isExternal    ) {
        super(
        );
        this.isDimension = isDimension;
        this.isExternal = isExternal;
    }


    public boolean getIsdimension() {
        return isDimension;
    }

    public void setIsdimension(boolean isDimension) {
        this.isDimension = isDimension;
    }
    public boolean getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(boolean isExternal) {
        this.isExternal = isExternal;
    }

    public PiServiceComposition_CompositionServiceModel getPiservicecomposition_compositionservicemodel() {
        return piservicecomposition_compositionservicemodel;
    }

    public void setPiservicecomposition_compositionservicemodel(PiServiceComposition_CompositionServiceModel piservicecomposition_compositionservicemodel) {
        this.piservicecomposition_compositionservicemodel = piservicecomposition_compositionservicemodel;
    }
    public PiServiceComposition_ActivityPartition getPiservicecomposition_activitypartition() {
        return piservicecomposition_activitypartition;
    }

    public void setPiservicecomposition_activitypartition(PiServiceComposition_ActivityPartition piservicecomposition_activitypartition) {
        this.piservicecomposition_activitypartition = piservicecomposition_activitypartition;
    }

}