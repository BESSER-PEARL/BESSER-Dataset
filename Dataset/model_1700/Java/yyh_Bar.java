





import java.util.List;
import java.util.ArrayList;

public class yyh_Bar  {

    private String id;





    private yyh_NamedElement yyh_namedelement;




    private yyh_Output yyh_output;


    public yyh_Bar(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public yyh_NamedElement getYyh_namedelement() {
        return yyh_namedelement;
    }

    public void setYyh_namedelement(yyh_NamedElement yyh_namedelement) {
        this.yyh_namedelement = yyh_namedelement;
    }
    public yyh_Output getYyh_output() {
        return yyh_output;
    }

    public void setYyh_output(yyh_Output yyh_output) {
        this.yyh_output = yyh_output;
    }

}