





import java.util.List;
import java.util.ArrayList;

public class yyg_Bar  {

    private String id;





    private yyg_Output yyg_output;




    private yyg_NamedElement yyg_namedelement;


    public yyg_Bar(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public yyg_Output getYyg_output() {
        return yyg_output;
    }

    public void setYyg_output(yyg_Output yyg_output) {
        this.yyg_output = yyg_output;
    }
    public yyg_NamedElement getYyg_namedelement() {
        return yyg_namedelement;
    }

    public void setYyg_namedelement(yyg_NamedElement yyg_namedelement) {
        this.yyg_namedelement = yyg_namedelement;
    }

}