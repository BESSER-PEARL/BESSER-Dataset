





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_NTierConnectionContent  {

    private String nTierName;
    private String ntierconnection;





    private softGalleryLanguage_NTiersConnections softgallerylanguage_ntiersconnections;


    public softGalleryLanguage_NTierConnectionContent(
        String nTierName,        String ntierconnection    ) {
        this.nTierName = nTierName;
        this.ntierconnection = ntierconnection;
    }


    public String getNtiername() {
        return nTierName;
    }

    public void setNtiername(String nTierName) {
        this.nTierName = nTierName;
    }
    public String getNtierconnection() {
        return ntierconnection;
    }

    public void setNtierconnection(String ntierconnection) {
        this.ntierconnection = ntierconnection;
    }

    public softGalleryLanguage_NTiersConnections getSoftgallerylanguage_ntiersconnections() {
        return softgallerylanguage_ntiersconnections;
    }

    public void setSoftgallerylanguage_ntiersconnections(softGalleryLanguage_NTiersConnections softgallerylanguage_ntiersconnections) {
        this.softgallerylanguage_ntiersconnections = softgallerylanguage_ntiersconnections;
    }

}