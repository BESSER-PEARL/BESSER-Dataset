





import java.util.List;
import java.util.ArrayList;

public class shr5_Localization  {

    private int page;
    private String local;
    private String name;





    private shr5_Identifiable shr5_identifiable;


    public shr5_Localization(
        int page,        String local,        String name    ) {
        this.page = page;
        this.local = local;
        this.name = name;
    }


    public int getPage() {
        return page;
    }

    public void setPage(int page) {
        this.page = page;
    }
    public String getLocal() {
        return local;
    }

    public void setLocal(String local) {
        this.local = local;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public shr5_Identifiable getShr5_identifiable() {
        return shr5_identifiable;
    }

    public void setShr5_identifiable(shr5_Identifiable shr5_identifiable) {
        this.shr5_identifiable = shr5_identifiable;
    }

}