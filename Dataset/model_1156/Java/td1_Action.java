





import java.util.List;
import java.util.ArrayList;

public class td1_Action  {

    private String Name;
    private String codeFiacre;
    private String Body;



    public td1_Action(
        String Name,        String codeFiacre,        String Body    ) {
        this.Name = Name;
        this.codeFiacre = codeFiacre;
        this.Body = Body;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
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


}