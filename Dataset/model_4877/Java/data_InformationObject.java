





import java.util.List;
import java.util.ArrayList;

public class data_InformationObject extends Item {

    private String verifiedName;
    private String alternativeNames;
    private String name;



    public data_InformationObject(
        String verifiedName,        String alternativeNames,        String name    ) {
        super(
        );
        this.verifiedName = verifiedName;
        this.alternativeNames = alternativeNames;
        this.name = name;
    }


    public String getVerifiedname() {
        return verifiedName;
    }

    public void setVerifiedname(String verifiedName) {
        this.verifiedName = verifiedName;
    }
    public String getAlternativenames() {
        return alternativeNames;
    }

    public void setAlternativenames(String alternativeNames) {
        this.alternativeNames = alternativeNames;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}