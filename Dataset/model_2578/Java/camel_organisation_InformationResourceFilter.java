





import java.util.List;
import java.util.ArrayList;

public class camel_organisation_InformationResourceFilter extends ResourceFilter {

    private String informationResourcePath;
    private boolean everyInformationResource;



    public camel_organisation_InformationResourceFilter(
        String informationResourcePath,        boolean everyInformationResource    ) {
        super(
        );
        this.informationResourcePath = informationResourcePath;
        this.everyInformationResource = everyInformationResource;
    }


    public String getInformationresourcepath() {
        return informationResourcePath;
    }

    public void setInformationresourcepath(String informationResourcePath) {
        this.informationResourcePath = informationResourcePath;
    }
    public boolean getEveryinformationresource() {
        return everyInformationResource;
    }

    public void setEveryinformationresource(boolean everyInformationResource) {
        this.everyInformationResource = everyInformationResource;
    }


}