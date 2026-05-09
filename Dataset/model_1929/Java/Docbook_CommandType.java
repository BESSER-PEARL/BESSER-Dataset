





import java.util.List;
import java.util.ArrayList;

public class Docbook_CommandType  {

    private String mixed;





    private Docbook_CmdsynopsisType docbook_cmdsynopsistype;


    public Docbook_CommandType(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Docbook_CmdsynopsisType getDocbook_cmdsynopsistype() {
        return docbook_cmdsynopsistype;
    }

    public void setDocbook_cmdsynopsistype(Docbook_CmdsynopsisType docbook_cmdsynopsistype) {
        this.docbook_cmdsynopsistype = docbook_cmdsynopsistype;
    }

}