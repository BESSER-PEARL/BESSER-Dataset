





import java.util.List;
import java.util.ArrayList;

public class TreeNodeXML_XMLTreeNode  {

    private String LocalName;
    private String ElementText;





    private TreeNodeXML_XMLTreeNode treenodexml_xmltreenode;


    public TreeNodeXML_XMLTreeNode(
        String LocalName,        String ElementText    ) {
        this.LocalName = LocalName;
        this.ElementText = ElementText;
    }


    public String getLocalname() {
        return LocalName;
    }

    public void setLocalname(String LocalName) {
        this.LocalName = LocalName;
    }
    public String getElementtext() {
        return ElementText;
    }

    public void setElementtext(String ElementText) {
        this.ElementText = ElementText;
    }

    public TreeNodeXML_XMLTreeNode getTreenodexml_xmltreenode() {
        return treenodexml_xmltreenode;
    }

    public void setTreenodexml_xmltreenode(TreeNodeXML_XMLTreeNode treenodexml_xmltreenode) {
        this.treenodexml_xmltreenode = treenodexml_xmltreenode;
    }

}