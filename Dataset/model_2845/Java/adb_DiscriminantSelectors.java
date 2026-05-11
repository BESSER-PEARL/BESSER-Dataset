





import java.util.List;
import java.util.ArrayList;

public class adb_DiscriminantSelectors  {

    private String discriminantSelectorName;





    private adb_DiscriminantAssociation adb_discriminantassociation;


    public adb_DiscriminantSelectors(
        String discriminantSelectorName    ) {
        this.discriminantSelectorName = discriminantSelectorName;
    }


    public String getDiscriminantselectorname() {
        return discriminantSelectorName;
    }

    public void setDiscriminantselectorname(String discriminantSelectorName) {
        this.discriminantSelectorName = discriminantSelectorName;
    }

    public adb_DiscriminantAssociation getAdb_discriminantassociation() {
        return adb_discriminantassociation;
    }

    public void setAdb_discriminantassociation(adb_DiscriminantAssociation adb_discriminantassociation) {
        this.adb_discriminantassociation = adb_discriminantassociation;
    }

}