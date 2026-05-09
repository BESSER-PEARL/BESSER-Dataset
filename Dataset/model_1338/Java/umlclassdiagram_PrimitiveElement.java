





import java.util.List;
import java.util.ArrayList;

public class umlclassdiagram_PrimitiveElement extends NamedElement {

    private String type;





    private umlclassdiagram_ClassDiagram umlclassdiagram_classdiagram;


    public umlclassdiagram_PrimitiveElement(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public umlclassdiagram_ClassDiagram getUmlclassdiagram_classdiagram() {
        return umlclassdiagram_classdiagram;
    }

    public void setUmlclassdiagram_classdiagram(umlclassdiagram_ClassDiagram umlclassdiagram_classdiagram) {
        this.umlclassdiagram_classdiagram = umlclassdiagram_classdiagram;
    }

}