





import java.util.List;
import java.util.ArrayList;

public class camel_deployment_VMRequirementSet  {

    private String name;





    private QuantitativeHardwareRequirement quantitativehardwarerequirement;




    private QualitativeHardwareRequirement qualitativehardwarerequirement;




    private OSOrImageRequirement osorimagerequirement;


    public camel_deployment_VMRequirementSet(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public QuantitativeHardwareRequirement getQuantitativehardwarerequirement() {
        return quantitativehardwarerequirement;
    }

    public void setQuantitativehardwarerequirement(QuantitativeHardwareRequirement quantitativehardwarerequirement) {
        this.quantitativehardwarerequirement = quantitativehardwarerequirement;
    }
    public QualitativeHardwareRequirement getQualitativehardwarerequirement() {
        return qualitativehardwarerequirement;
    }

    public void setQualitativehardwarerequirement(QualitativeHardwareRequirement qualitativehardwarerequirement) {
        this.qualitativehardwarerequirement = qualitativehardwarerequirement;
    }
    public OSOrImageRequirement getOsorimagerequirement() {
        return osorimagerequirement;
    }

    public void setOsorimagerequirement(OSOrImageRequirement osorimagerequirement) {
        this.osorimagerequirement = osorimagerequirement;
    }

}