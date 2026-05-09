





import java.util.List;
import java.util.ArrayList;

public class umlclassdiagram_Constraint  {

    private String id;





    private List<umlclassdiagram_RootCS> umlclassdiagram_rootcss;




    private umlclassdiagram_ClassDiagram umlclassdiagram_classdiagram;


    public umlclassdiagram_Constraint(
        String id    ) {
        this.id = id;
        this.umlclassdiagram_rootcss = new ArrayList<>();
    }

    public umlclassdiagram_Constraint(
        String id        ArrayList<umlclassdiagram_RootCS> umlclassdiagram_rootcss    ) {
        this.id = id;
        this.umlclassdiagram_rootcss = umlclassdiagram_rootcss;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<umlclassdiagram_RootCS> getUmlclassdiagram_rootcss() {
        return umlclassdiagram_rootcss;
    }

    public void addUmlclassdiagram_rootcs(Umlclassdiagram_rootcs umlclassdiagram_rootcs) {
        this.umlclassdiagram_rootcss.add(umlclassdiagram_rootcs);
    }
    public umlclassdiagram_ClassDiagram getUmlclassdiagram_classdiagram() {
        return umlclassdiagram_classdiagram;
    }

    public void setUmlclassdiagram_classdiagram(umlclassdiagram_ClassDiagram umlclassdiagram_classdiagram) {
        this.umlclassdiagram_classdiagram = umlclassdiagram_classdiagram;
    }

}