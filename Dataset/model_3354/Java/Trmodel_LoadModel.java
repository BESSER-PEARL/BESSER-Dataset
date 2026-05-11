





import java.util.List;
import java.util.ArrayList;

public class Trmodel_LoadModel  {

    private String url;





    private Trmodel_loader trmodel_loader;


    public Trmodel_LoadModel(
        String url    ) {
        this.url = url;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public Trmodel_loader getTrmodel_loader() {
        return trmodel_loader;
    }

    public void setTrmodel_loader(Trmodel_loader trmodel_loader) {
        this.trmodel_loader = trmodel_loader;
    }

}