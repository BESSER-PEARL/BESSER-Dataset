





import java.util.List;
import java.util.ArrayList;

public class moba_MobaGeneratorIDFeature extends MobaGeneratorFeature {

    private String generatorVersion;
    private String generatorId;



    public moba_MobaGeneratorIDFeature(
        String generatorVersion,        String generatorId    ) {
        super(
        );
        this.generatorVersion = generatorVersion;
        this.generatorId = generatorId;
    }


    public String getGeneratorversion() {
        return generatorVersion;
    }

    public void setGeneratorversion(String generatorVersion) {
        this.generatorVersion = generatorVersion;
    }
    public String getGeneratorid() {
        return generatorId;
    }

    public void setGeneratorid(String generatorId) {
        this.generatorId = generatorId;
    }


}