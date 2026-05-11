





import java.util.List;
import java.util.ArrayList;

public class frameweb_DAOClass extends Class {

    private String prefix;
    private String sufix;
    private String infix;



    public frameweb_DAOClass(
        String prefix,        String sufix,        String infix    ) {
        super(
        );
        this.prefix = prefix;
        this.sufix = sufix;
        this.infix = infix;
    }


    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }
    public String getSufix() {
        return sufix;
    }

    public void setSufix(String sufix) {
        this.sufix = sufix;
    }
    public String getInfix() {
        return infix;
    }

    public void setInfix(String infix) {
        this.infix = infix;
    }


}