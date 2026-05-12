





import java.util.List;
import java.util.ArrayList;

public class latex_Abstracte  {

    private String abstracttext;
    private String abstractprefix;



    public latex_Abstracte(
        String abstracttext,        String abstractprefix    ) {
        this.abstracttext = abstracttext;
        this.abstractprefix = abstractprefix;
    }


    public String getAbstracttext() {
        return abstracttext;
    }

    public void setAbstracttext(String abstracttext) {
        this.abstracttext = abstracttext;
    }
    public String getAbstractprefix() {
        return abstractprefix;
    }

    public void setAbstractprefix(String abstractprefix) {
        this.abstractprefix = abstractprefix;
    }


}