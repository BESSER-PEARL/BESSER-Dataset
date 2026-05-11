





import java.util.List;
import java.util.ArrayList;

public class data_InformationObject extends Item {

    private String name;
    private String alternativeNames;
    private String verifiedName;



    public data_InformationObject(
        String name,        String alternativeNames,        String verifiedName    ) {
        super(
        );
        this.name = name;
        this.alternativeNames = alternativeNames;
        this.verifiedName = verifiedName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAlternativenames() {
        return alternativeNames;
    }

    public void setAlternativenames(String alternativeNames) {
        this.alternativeNames = alternativeNames;
    }
    public String getVerifiedname() {
        return verifiedName;
    }

    public void setVerifiedname(String verifiedName) {
        this.verifiedName = verifiedName;
    }


}