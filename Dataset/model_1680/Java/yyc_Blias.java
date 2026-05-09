





import java.util.List;
import java.util.ArrayList;

public class yyc_Blias  {

    private String id;





    private yyc_RelatedTo yyc_relatedto;


    public yyc_Blias(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public yyc_RelatedTo getYyc_relatedto() {
        return yyc_relatedto;
    }

    public void setYyc_relatedto(yyc_RelatedTo yyc_relatedto) {
        this.yyc_relatedto = yyc_relatedto;
    }

}