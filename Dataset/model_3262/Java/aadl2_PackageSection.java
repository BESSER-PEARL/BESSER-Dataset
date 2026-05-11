





import java.util.List;
import java.util.ArrayList;

public class aadl2_PackageSection extends Namespace {

    private String noProperties;
    private String noAnnexes;



    public aadl2_PackageSection(
        String noProperties,        String noAnnexes    ) {
        super(
        );
        this.noProperties = noProperties;
        this.noAnnexes = noAnnexes;
    }


    public String getNoproperties() {
        return noProperties;
    }

    public void setNoproperties(String noProperties) {
        this.noProperties = noProperties;
    }
    public String getNoannexes() {
        return noAnnexes;
    }

    public void setNoannexes(String noAnnexes) {
        this.noAnnexes = noAnnexes;
    }


}