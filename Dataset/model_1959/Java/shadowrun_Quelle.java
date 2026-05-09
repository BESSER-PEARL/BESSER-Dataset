





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Quelle  {

    private String page;





    private shadowrun_SourceBook shadowrun_sourcebook;


    public shadowrun_Quelle(
        String page    ) {
        this.page = page;
    }


    public String getPage() {
        return page;
    }

    public void setPage(String page) {
        this.page = page;
    }

    public shadowrun_SourceBook getShadowrun_sourcebook() {
        return shadowrun_sourcebook;
    }

    public void setShadowrun_sourcebook(shadowrun_SourceBook shadowrun_sourcebook) {
        this.shadowrun_sourcebook = shadowrun_sourcebook;
    }

}