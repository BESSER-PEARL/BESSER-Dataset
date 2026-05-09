





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_Store extends MediaSource {

    private String url;
    private String name;



    public MediaLibrary_Store(
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