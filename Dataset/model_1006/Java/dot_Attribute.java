





import java.util.List;
import java.util.ArrayList;

public class dot_Attribute extends Statement {

    private String name;
    private String value;





    private dot_AttributeStatement dot_attributestatement;




    private dot_EdgeStatement dot_edgestatement;




    private dot_NodeStatement dot_nodestatement;


    public dot_Attribute(
        String name,        String value    ) {
        super(
        );
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public dot_AttributeStatement getDot_attributestatement() {
        return dot_attributestatement;
    }

    public void setDot_attributestatement(dot_AttributeStatement dot_attributestatement) {
        this.dot_attributestatement = dot_attributestatement;
    }
    public dot_EdgeStatement getDot_edgestatement() {
        return dot_edgestatement;
    }

    public void setDot_edgestatement(dot_EdgeStatement dot_edgestatement) {
        this.dot_edgestatement = dot_edgestatement;
    }
    public dot_NodeStatement getDot_nodestatement() {
        return dot_nodestatement;
    }

    public void setDot_nodestatement(dot_NodeStatement dot_nodestatement) {
        this.dot_nodestatement = dot_nodestatement;
    }

}