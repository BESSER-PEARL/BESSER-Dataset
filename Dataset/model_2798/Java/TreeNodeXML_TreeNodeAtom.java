





import java.util.List;
import java.util.ArrayList;

public class TreeNodeXML_TreeNodeAtom  {

    private String AttributeLocalName;
    private String AttributeValue;





    private TreeNodeXML_XMLTreeNode treenodexml_xmltreenode;


    public TreeNodeXML_TreeNodeAtom(
        String AttributeLocalName,        String AttributeValue    ) {
        this.AttributeLocalName = AttributeLocalName;
        this.AttributeValue = AttributeValue;
    }


    public String getAttributelocalname() {
        return AttributeLocalName;
    }

    public void setAttributelocalname(String AttributeLocalName) {
        this.AttributeLocalName = AttributeLocalName;
    }
    public String getAttributevalue() {
        return AttributeValue;
    }

    public void setAttributevalue(String AttributeValue) {
        this.AttributeValue = AttributeValue;
    }

    public TreeNodeXML_XMLTreeNode getTreenodexml_xmltreenode() {
        return treenodexml_xmltreenode;
    }

    public void setTreenodexml_xmltreenode(TreeNodeXML_XMLTreeNode treenodexml_xmltreenode) {
        this.treenodexml_xmltreenode = treenodexml_xmltreenode;
    }

}