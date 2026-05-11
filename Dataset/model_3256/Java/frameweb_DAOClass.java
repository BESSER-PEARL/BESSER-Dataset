





import java.util.List;
import java.util.ArrayList;

public class frameweb_DAOClass extends Class {

    private String infix;
    private String sufix;
    private String prefix;



    public frameweb_DAOClass(
        String infix,        String sufix,        String prefix    ) {
        super(
        );
        this.infix = infix;
        this.sufix = sufix;
        this.prefix = prefix;
    }


    public String getInfix() {
        return infix;
    }

    public void setInfix(String infix) {
        this.infix = infix;
    }
    public String getSufix() {
        return sufix;
    }

    public void setSufix(String sufix) {
        this.sufix = sufix;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }


}