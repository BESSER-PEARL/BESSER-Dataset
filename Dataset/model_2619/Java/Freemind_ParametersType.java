





import java.util.List;
import java.util.ArrayList;

public class Freemind_ParametersType  {

    private String RemindUserAt;





    private Freemind_DocumentRoot freemind_documentroot;


    public Freemind_ParametersType(
        String RemindUserAt    ) {
        this.RemindUserAt = RemindUserAt;
    }


    public String getReminduserat() {
        return RemindUserAt;
    }

    public void setReminduserat(String RemindUserAt) {
        this.RemindUserAt = RemindUserAt;
    }

    public Freemind_DocumentRoot getFreemind_documentroot() {
        return freemind_documentroot;
    }

    public void setFreemind_documentroot(Freemind_DocumentRoot freemind_documentroot) {
        this.freemind_documentroot = freemind_documentroot;
    }

}