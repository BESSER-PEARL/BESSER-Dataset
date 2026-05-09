





import java.util.List;
import java.util.ArrayList;

public class fiacremm_Guard extends EModelElement {

    private String Body;
    private String codeFiacre;
    private String Name;



    public fiacremm_Guard(
        String Body,        String codeFiacre,        String Name    ) {
        super(
        );
        this.Body = Body;
        this.codeFiacre = codeFiacre;
        this.Name = Name;
    }


    public String getBody() {
        return Body;
    }

    public void setBody(String Body) {
        this.Body = Body;
    }
    public String getCodefiacre() {
        return codeFiacre;
    }

    public void setCodefiacre(String codeFiacre) {
        this.codeFiacre = codeFiacre;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}