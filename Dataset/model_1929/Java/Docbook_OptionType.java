





import java.util.List;
import java.util.ArrayList;

public class Docbook_OptionType  {

    private String mixed;





    private Docbook_ArgType docbook_argtype;


    public Docbook_OptionType(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Docbook_ArgType getDocbook_argtype() {
        return docbook_argtype;
    }

    public void setDocbook_argtype(Docbook_ArgType docbook_argtype) {
        this.docbook_argtype = docbook_argtype;
    }

}