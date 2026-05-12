





import java.util.List;
import java.util.ArrayList;

public class MediaPool  {

    private String assets;
    private String name;





    private MediaPool mediapool;


    public MediaPool(
        String assets,        String name    ) {
        this.assets = assets;
        this.name = name;
    }


    public String getAssets() {
        return assets;
    }

    public void setAssets(String assets) {
        this.assets = assets;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MediaPool getMediapool() {
        return mediapool;
    }

    public void setMediapool(MediaPool mediapool) {
        this.mediapool = mediapool;
    }

}