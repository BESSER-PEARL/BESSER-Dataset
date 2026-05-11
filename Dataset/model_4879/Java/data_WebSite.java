





import java.util.List;
import java.util.ArrayList;

public class data_WebSite extends MetaInformation {

    private String adress;
    private String title;



    public data_WebSite(
        String adress,        String title    ) {
        super(
        );
        this.adress = adress;
        this.title = title;
    }


    public String getAdress() {
        return adress;
    }

    public void setAdress(String adress) {
        this.adress = adress;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}