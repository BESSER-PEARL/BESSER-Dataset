





import java.util.List;
import java.util.ArrayList;

public class standard_Infector extends Modifiable, NodeDecorator {

    private String populationIdentifier;
    private String targetURI;
    private String diseaseName;
    private boolean infectPercentage;
    private String targetISOKey;





    private standard_InfectorInoculatorCollection standard_infectorinoculatorcollection;


    public standard_Infector(
        String populationIdentifier,        String targetURI,        String diseaseName,        boolean infectPercentage,        String targetISOKey    ) {
        super(
        );
        this.populationIdentifier = populationIdentifier;
        this.targetURI = targetURI;
        this.diseaseName = diseaseName;
        this.infectPercentage = infectPercentage;
        this.targetISOKey = targetISOKey;
    }


    public String getPopulationidentifier() {
        return populationIdentifier;
    }

    public void setPopulationidentifier(String populationIdentifier) {
        this.populationIdentifier = populationIdentifier;
    }
    public String getTargeturi() {
        return targetURI;
    }

    public void setTargeturi(String targetURI) {
        this.targetURI = targetURI;
    }
    public String getDiseasename() {
        return diseaseName;
    }

    public void setDiseasename(String diseaseName) {
        this.diseaseName = diseaseName;
    }
    public boolean getInfectpercentage() {
        return infectPercentage;
    }

    public void setInfectpercentage(boolean infectPercentage) {
        this.infectPercentage = infectPercentage;
    }
    public String getTargetisokey() {
        return targetISOKey;
    }

    public void setTargetisokey(String targetISOKey) {
        this.targetISOKey = targetISOKey;
    }

    public standard_InfectorInoculatorCollection getStandard_infectorinoculatorcollection() {
        return standard_infectorinoculatorcollection;
    }

    public void setStandard_infectorinoculatorcollection(standard_InfectorInoculatorCollection standard_infectorinoculatorcollection) {
        this.standard_infectorinoculatorcollection = standard_infectorinoculatorcollection;
    }

}