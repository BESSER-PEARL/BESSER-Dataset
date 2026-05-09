





import java.util.List;
import java.util.ArrayList;

public class shr5_Quelle extends Identifiable {

    private String page;





    private shr5_SourceBook shr5_sourcebook;


    public shr5_Quelle(
        String page    ) {
        super(
        );
        this.page = page;
    }


    public String getPage() {
        return page;
    }

    public void setPage(String page) {
        this.page = page;
    }

    public shr5_SourceBook getShr5_sourcebook() {
        return shr5_sourcebook;
    }

    public void setShr5_sourcebook(shr5_SourceBook shr5_sourcebook) {
        this.shr5_sourcebook = shr5_sourcebook;
    }

}