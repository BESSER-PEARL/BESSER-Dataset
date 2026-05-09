





import java.util.List;
import java.util.ArrayList;

public class umlclassdiagram_ParameterCS  {

    private String name;





    private umlclassdiagram_OperationCS umlclassdiagram_operationcs;




    private umlclassdiagram_PathNameCS umlclassdiagram_pathnamecs;


    public umlclassdiagram_ParameterCS(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public umlclassdiagram_OperationCS getUmlclassdiagram_operationcs() {
        return umlclassdiagram_operationcs;
    }

    public void setUmlclassdiagram_operationcs(umlclassdiagram_OperationCS umlclassdiagram_operationcs) {
        this.umlclassdiagram_operationcs = umlclassdiagram_operationcs;
    }
    public umlclassdiagram_PathNameCS getUmlclassdiagram_pathnamecs() {
        return umlclassdiagram_pathnamecs;
    }

    public void setUmlclassdiagram_pathnamecs(umlclassdiagram_PathNameCS umlclassdiagram_pathnamecs) {
        this.umlclassdiagram_pathnamecs = umlclassdiagram_pathnamecs;
    }

}