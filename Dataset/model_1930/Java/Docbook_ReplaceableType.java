





import java.util.List;
import java.util.ArrayList;

public class Docbook_ReplaceableType  {

    private String mixed;





    private Docbook_OptionType docbook_optiontype;




    private Docbook_ArgType docbook_argtype;


    public Docbook_ReplaceableType(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Docbook_OptionType getDocbook_optiontype() {
        return docbook_optiontype;
    }

    public void setDocbook_optiontype(Docbook_OptionType docbook_optiontype) {
        this.docbook_optiontype = docbook_optiontype;
    }
    public Docbook_ArgType getDocbook_argtype() {
        return docbook_argtype;
    }

    public void setDocbook_argtype(Docbook_ArgType docbook_argtype) {
        this.docbook_argtype = docbook_argtype;
    }

}