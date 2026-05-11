





import java.util.List;
import java.util.ArrayList;

public class core_COREModelElement extends CORENamedElement {

    private String partiality;
    private String visibility;





    private core_COREInterface core_coreinterface;




    private core_COREModel core_coremodel;




    private core_COREInterface core_coreinterface;


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

    public core_COREInterface getCore_coreinterface() {
        return core_coreinterface;
    }

    public void setCore_coreinterface(core_COREInterface core_coreinterface) {
        this.core_coreinterface = core_coreinterface;
    }
    public core_COREModel getCore_coremodel() {
        return core_coremodel;
    }

    public void setCore_coremodel(core_COREModel core_coremodel) {
        this.core_coremodel = core_coremodel;
    }
    public core_COREInterface getCore_coreinterface() {
        return core_coreinterface;
    }

    public void setCore_coreinterface(core_COREInterface core_coreinterface) {
        this.core_coreinterface = core_coreinterface;
    }

}