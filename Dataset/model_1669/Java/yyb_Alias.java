





import java.util.List;
import java.util.ArrayList;

public class yyb_Alias  {

    private String id;





    private yyb_RelatedTo yyb_relatedto;


    public yyb_Alias(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public yyb_RelatedTo getYyb_relatedto() {
        return yyb_relatedto;
    }

    public void setYyb_relatedto(yyb_RelatedTo yyb_relatedto) {
        this.yyb_relatedto = yyb_relatedto;
    }

}