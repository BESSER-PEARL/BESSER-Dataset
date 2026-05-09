





import java.util.List;
import java.util.ArrayList;

public class umlclassdiagram_OperationCS  {

    private String name;





    private umlclassdiagram_PathNameCS umlclassdiagram_pathnamecs;




    private umlclassdiagram_ClassCS umlclassdiagram_classcs;


    public umlclassdiagram_OperationCS(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public umlclassdiagram_PathNameCS getUmlclassdiagram_pathnamecs() {
        return umlclassdiagram_pathnamecs;
    }

    public void setUmlclassdiagram_pathnamecs(umlclassdiagram_PathNameCS umlclassdiagram_pathnamecs) {
        this.umlclassdiagram_pathnamecs = umlclassdiagram_pathnamecs;
    }
    public umlclassdiagram_ClassCS getUmlclassdiagram_classcs() {
        return umlclassdiagram_classcs;
    }

    public void setUmlclassdiagram_classcs(umlclassdiagram_ClassCS umlclassdiagram_classcs) {
        this.umlclassdiagram_classcs = umlclassdiagram_classcs;
    }

}