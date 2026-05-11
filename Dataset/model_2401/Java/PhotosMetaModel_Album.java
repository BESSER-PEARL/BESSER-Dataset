





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Album extends Entities {

    private String url;
    private String name;



    public PhotosMetaModel_Album(
        String url,        String name    ) {
        super(
        );
        this.url = url;
        this.name = name;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}