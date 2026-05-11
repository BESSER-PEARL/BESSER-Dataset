





import java.util.List;
import java.util.ArrayList;

public class Freemind_FontType  {

    private String Bold;
    private String Italic;
    private String Name;
    private String Size;





    private Freemind_DocumentRoot freemind_documentroot;




    private Freemind_NodeType freemind_nodetype;


    public Freemind_FontType(
        String Bold,        String Italic,        String Name,        String Size    ) {
        this.Bold = Bold;
        this.Italic = Italic;
        this.Name = Name;
        this.Size = Size;
    }


    public String getBold() {
        return Bold;
    }

    public void setBold(String Bold) {
        this.Bold = Bold;
    }
    public String getItalic() {
        return Italic;
    }

    public void setItalic(String Italic) {
        this.Italic = Italic;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getSize() {
        return Size;
    }

    public void setSize(String Size) {
        this.Size = Size;
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