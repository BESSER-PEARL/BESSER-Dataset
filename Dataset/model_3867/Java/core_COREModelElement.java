





import java.util.List;
import java.util.ArrayList;

public class core_COREModelElement extends CORENamedElement {

    private String partiality;
    private String visibility;





    private core_COREModel core_coremodel;


    public core_COREModelElement(
        String partiality,        String visibility    ) {
        super(
        );
        this.partiality = partiality;
        this.visibility = visibility;
    }


    public String getPartiality() {
        return partiality;
    }

    public void setPartiality(String partiality) {
        this.partiality = partiality;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public core_COREModel getCore_coremodel() {
        return core_coremodel;
    }

    public void setCore_coremodel(core_COREModel core_coremodel) {
        this.core_coremodel = core_coremodel;
    }

}