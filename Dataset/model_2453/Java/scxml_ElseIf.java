





import java.util.List;
import java.util.ArrayList;

public class scxml_ElseIf  {

    private String cond;





    private scxml_If scxml_if;


    public scxml_ElseIf(
        String cond    ) {
        this.cond = cond;
    }


    public String getCond() {
        return cond;
    }

    public void setCond(String cond) {
        this.cond = cond;
    }

    public scxml_If getScxml_if() {
        return scxml_if;
    }

    public void setScxml_if(scxml_If scxml_if) {
        this.scxml_if = scxml_if;
    }

}