





import java.util.List;
import java.util.ArrayList;

public class Service  {

    private String Info;
    private String Terms;



    public Service(
        String Info,        String Terms    ) {
        this.Info = Info;
        this.Terms = Terms;
    }


    public String getInfo() {
        return Info;
    }

    public void setInfo(String Info) {
        this.Info = Info;
    }
    public String getTerms() {
        return Terms;
    }

    public void setTerms(String Terms) {
        this.Terms = Terms;
    }


}