





import java.util.List;
import java.util.ArrayList;

public class yyf_Output  {

    private String id;





    private yyf_Bar yyf_bar;




    private yyf_Base yyf_base;


    public yyf_Output(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public yyf_Bar getYyf_bar() {
        return yyf_bar;
    }

    public void setYyf_bar(yyf_Bar yyf_bar) {
        this.yyf_bar = yyf_bar;
    }
    public yyf_Base getYyf_base() {
        return yyf_base;
    }

    public void setYyf_base(yyf_Base yyf_base) {
        this.yyf_base = yyf_base;
    }

}