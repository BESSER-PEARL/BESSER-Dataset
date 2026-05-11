





import java.util.List;
import java.util.ArrayList;

public class express_Line  {

    private String text;





    private express_IfStatement express_ifstatement;




    private express_ConstantVal express_constantval;




    private express_LocalVar express_localvar;


    public express_Line(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public express_IfStatement getExpress_ifstatement() {
        return express_ifstatement;
    }

    public void setExpress_ifstatement(express_IfStatement express_ifstatement) {
        this.express_ifstatement = express_ifstatement;
    }
    public express_ConstantVal getExpress_constantval() {
        return express_constantval;
    }

    public void setExpress_constantval(express_ConstantVal express_constantval) {
        this.express_constantval = express_constantval;
    }
    public express_LocalVar getExpress_localvar() {
        return express_localvar;
    }

    public void setExpress_localvar(express_LocalVar express_localvar) {
        this.express_localvar = express_localvar;
    }

}