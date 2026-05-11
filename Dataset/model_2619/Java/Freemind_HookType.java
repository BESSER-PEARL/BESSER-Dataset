





import java.util.List;
import java.util.ArrayList;

public class Freemind_HookType  {

    private String Name;





    private Freemind_ParametersType freemind_parameterstype;




    private Freemind_DocumentRoot freemind_documentroot;




    private Freemind_NodeType freemind_nodetype;


    public Freemind_HookType(
        String Name    ) {
        this.Name = Name;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Freemind_ParametersType getFreemind_parameterstype() {
        return freemind_parameterstype;
    }

    public void setFreemind_parameterstype(Freemind_ParametersType freemind_parameterstype) {
        this.freemind_parameterstype = freemind_parameterstype;
    }
    public Freemind_DocumentRoot getFreemind_documentroot() {
        return freemind_documentroot;
    }

    public void setFreemind_documentroot(Freemind_DocumentRoot freemind_documentroot) {
        this.freemind_documentroot = freemind_documentroot;
    }
    public Freemind_NodeType getFreemind_nodetype() {
        return freemind_nodetype;
    }

    public void setFreemind_nodetype(Freemind_NodeType freemind_nodetype) {
        this.freemind_nodetype = freemind_nodetype;
    }

}