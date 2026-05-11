





import java.util.List;
import java.util.ArrayList;

public class collection_RemoteCollection extends ItemsCollection {

    private String remoteURL;



    public collection_RemoteCollection(
        String remoteURL    ) {
        super(
        );
        this.remoteURL = remoteURL;
    }


    public String getRemoteurl() {
        return remoteURL;
    }

    public void setRemoteurl(String remoteURL) {
        this.remoteURL = remoteURL;
    }


}