





import java.util.List;
import java.util.ArrayList;

public class core_PlatformDisposition  {

    private boolean platformDependant;
    private String platformID;



    public core_PlatformDisposition(
        boolean platformDependant,        String platformID    ) {
        this.platformDependant = platformDependant;
        this.platformID = platformID;
    }


    public boolean getPlatformdependant() {
        return platformDependant;
    }

    public void setPlatformdependant(boolean platformDependant) {
        this.platformDependant = platformDependant;
    }
    public String getPlatformid() {
        return platformID;
    }

    public void setPlatformid(String platformID) {
        this.platformID = platformID;
    }


}