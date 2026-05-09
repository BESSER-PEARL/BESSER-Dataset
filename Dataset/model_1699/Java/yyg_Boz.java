





import java.util.List;
import java.util.ArrayList;

public class yyg_Boz extends NamedElement {

    private String since;





    private List<yyg_Boz> yyg_bozs;




    private yyg_Base yyg_base;




    private yyg_Base yyg_base;


    public yyg_Boz(
        String since    ) {
        super(
        );
        this.since = since;
        this.yyg_bozs = new ArrayList<>();
    }

    public yyg_Boz(
        String since        ArrayList<yyg_Boz> yyg_bozs    ) {
        this.since = since;
        this.yyg_bozs = yyg_bozs;
    }

    public String getSince() {
        return since;
    }

    public void setSince(String since) {
        this.since = since;
    }

    public List<yyg_Boz> getYyg_bozs() {
        return yyg_bozs;
    }

    public void addYyg_boz(Yyg_boz yyg_boz) {
        this.yyg_bozs.add(yyg_boz);
    }
    public yyg_Base getYyg_base() {
        return yyg_base;
    }

    public void setYyg_base(yyg_Base yyg_base) {
        this.yyg_base = yyg_base;
    }
    public yyg_Base getYyg_base() {
        return yyg_base;
    }

    public void setYyg_base(yyg_Base yyg_base) {
        this.yyg_base = yyg_base;
    }

}