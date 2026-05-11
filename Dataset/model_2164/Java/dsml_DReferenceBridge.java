





import java.util.List;
import java.util.ArrayList;

public class dsml_DReferenceBridge extends DModelElementBridge {






    private dsml_DEdge dsml_dedge;




    private dsml_DContainedElement dsml_dcontainedelement;




    private dsml_DLink dsml_dlink;


    public dsml_DReferenceBridge(
    ) {
        super(
        );
    }



    public dsml_DEdge getDsml_dedge() {
        return dsml_dedge;
    }

    public void setDsml_dedge(dsml_DEdge dsml_dedge) {
        this.dsml_dedge = dsml_dedge;
    }
    public dsml_DContainedElement getDsml_dcontainedelement() {
        return dsml_dcontainedelement;
    }

    public void setDsml_dcontainedelement(dsml_DContainedElement dsml_dcontainedelement) {
        this.dsml_dcontainedelement = dsml_dcontainedelement;
    }
    public dsml_DLink getDsml_dlink() {
        return dsml_dlink;
    }

    public void setDsml_dlink(dsml_DLink dsml_dlink) {
        this.dsml_dlink = dsml_dlink;
    }

}