





import java.util.List;
import java.util.ArrayList;

public class stext_StatechartDefinition  {

    private String namespace;





    private stext_StatechartRoot stext_statechartroot;


    public stext_StatechartDefinition(
        String namespace    ) {
        this.namespace = namespace;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }

    public stext_StatechartRoot getStext_statechartroot() {
        return stext_statechartroot;
    }

    public void setStext_statechartroot(stext_StatechartRoot stext_statechartroot) {
        this.stext_statechartroot = stext_statechartroot;
    }

}