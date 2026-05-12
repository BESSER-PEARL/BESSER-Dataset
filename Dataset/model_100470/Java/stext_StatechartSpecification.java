





import java.util.List;
import java.util.ArrayList;

public class stext_StatechartSpecification  {

    private String namespace;





    private stext_StatechartRoot stext_statechartroot;




    private List<stext_StatechartScope> stext_statechartscopes;


    public stext_StatechartSpecification(
        String namespace    ) {
        this.namespace = namespace;
        this.stext_statechartscopes = new ArrayList<>();
    }

    public stext_StatechartSpecification(
        String namespace        ArrayList<stext_StatechartScope> stext_statechartscopes    ) {
        this.namespace = namespace;
        this.stext_statechartscopes = stext_statechartscopes;
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
    public List<stext_StatechartScope> getStext_statechartscopes() {
        return stext_statechartscopes;
    }

    public void addStext_statechartscope(Stext_statechartscope stext_statechartscope) {
        this.stext_statechartscopes.add(stext_statechartscope);
    }

}