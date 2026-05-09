





import java.util.List;
import java.util.ArrayList;

public class fiacremm_Action extends EModelElement {

    private String codeFiacre;
    private String Body;
    private String Name;



    public fiacremm_Action(
        String codeFiacre,        String Body,        String Name    ) {
        super(
        );
        this.codeFiacre = codeFiacre;
        this.Body = Body;
        this.Name = Name;
    }


    public String getCodefiacre() {
        return codeFiacre;
    }

    public void setCodefiacre(String codeFiacre) {
        this.codeFiacre = codeFiacre;
    }
    public String getBody() {
        return Body;
    }

    public void setBody(String Body) {
        this.Body = Body;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}