





import java.util.List;
import java.util.ArrayList;

public class geoff_source_VectorSource extends Source {

    private String projection;
    private String url;
    private String format;



    public geoff_source_VectorSource(
        String projection,        String url,        String format    ) {
        super(
        );
        this.projection = projection;
        this.url = url;
        this.format = format;
    }


    public String getProjection() {
        return projection;
    }

    public void setProjection(String projection) {
        this.projection = projection;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }


}