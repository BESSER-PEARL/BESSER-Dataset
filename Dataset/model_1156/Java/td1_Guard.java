





import java.util.List;
import java.util.ArrayList;

public class td1_Guard  {

    private String codeFiacre;
    private String Name;
    private String Body;



    public td1_Guard(
        String codeFiacre,        String Name,        String Body    ) {
        this.codeFiacre = codeFiacre;
        this.Name = Name;
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
    public String getBody() {
        return Body;
    }

    public void setBody(String Body) {
        this.Body = Body;
    }


}