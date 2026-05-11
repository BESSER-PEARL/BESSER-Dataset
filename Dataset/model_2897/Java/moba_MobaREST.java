





import java.util.List;
import java.util.ArrayList;

public class moba_MobaREST extends MobaApplicationFeature {

    private String url;
    private String name;
    private boolean bigData;
    private String path;



    public moba_MobaREST(
        String url,        String name,        boolean bigData,        String path    ) {
        super(
        );
        this.url = url;
        this.name = name;
        this.bigData = bigData;
        this.path = path;
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
    public boolean getBigdata() {
        return bigData;
    }

    public void setBigdata(boolean bigData) {
        this.bigData = bigData;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }


}