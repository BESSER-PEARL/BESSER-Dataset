





import java.util.List;
import java.util.ArrayList;

public class Freemind_IconType  {

    private String Builtin;





    private Freemind_NodeType freemind_nodetype;




    private Freemind_DocumentRoot freemind_documentroot;


    public Freemind_IconType(
        String Builtin    ) {
        this.Builtin = Builtin;
    }


    public String getBuiltin() {
        return Builtin;
    }

    public void setBuiltin(String Builtin) {
        this.Builtin = Builtin;
    }

    public Freemind_NodeType getFreemind_nodetype() {
        return freemind_nodetype;
    }

    public void setFreemind_nodetype(Freemind_NodeType freemind_nodetype) {
        this.freemind_nodetype = freemind_nodetype;
    }
    public Freemind_DocumentRoot getFreemind_documentroot() {
        return freemind_documentroot;
    }

    public void setFreemind_documentroot(Freemind_DocumentRoot freemind_documentroot) {
        this.freemind_documentroot = freemind_documentroot;
    }

}