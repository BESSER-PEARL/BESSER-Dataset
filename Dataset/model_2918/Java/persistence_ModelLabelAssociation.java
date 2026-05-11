





import java.util.List;
import java.util.ArrayList;

public class persistence_ModelLabelAssociation extends ModelLabelFeature {

    private boolean isSourceAssociation;





    private persistence_ModelLabel persistence_modellabel;


    public persistence_ModelLabelAssociation(
        boolean isSourceAssociation    ) {
        super(
        );
        this.isSourceAssociation = isSourceAssociation;
    }


    public boolean getIssourceassociation() {
        return isSourceAssociation;
    }

    public void setIssourceassociation(boolean isSourceAssociation) {
        this.isSourceAssociation = isSourceAssociation;
    }

    public persistence_ModelLabel getPersistence_modellabel() {
        return persistence_modellabel;
    }

    public void setPersistence_modellabel(persistence_ModelLabel persistence_modellabel) {
        this.persistence_modellabel = persistence_modellabel;
    }

}