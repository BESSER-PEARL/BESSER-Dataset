





import java.util.List;
import java.util.ArrayList;

public class Docbook_FunctionType  {

    private String mixed;





    private Docbook_FuncdefType docbook_funcdeftype;


    public Docbook_FunctionType(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Docbook_FuncdefType getDocbook_funcdeftype() {
        return docbook_funcdeftype;
    }

    public void setDocbook_funcdeftype(Docbook_FuncdefType docbook_funcdeftype) {
        this.docbook_funcdeftype = docbook_funcdeftype;
    }

}