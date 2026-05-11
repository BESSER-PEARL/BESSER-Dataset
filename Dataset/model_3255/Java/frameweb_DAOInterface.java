





import java.util.List;
import java.util.ArrayList;

public class frameweb_DAOInterface extends Interface {

    private String infix;
    private String sufix;



    public frameweb_DAOInterface(
        String infix,        String sufix    ) {
        super(
        );
        this.infix = infix;
        this.sufix = sufix;
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


}