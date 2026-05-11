





import java.util.List;
import java.util.ArrayList;

public class rpslPerceptionGraphMetaModel_Element  {

    private String name;
    private String doc;





    private rpslPerceptionGraphMetaModel_PerceptionGraph rpslperceptiongraphmetamodel_perceptiongraph;


    public rpslPerceptionGraphMetaModel_Element(
        String name,        String doc    ) {
        this.name = name;
        this.doc = doc;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDoc() {
        return doc;
    }

    public void setDoc(String doc) {
        this.doc = doc;
    }

    public rpslPerceptionGraphMetaModel_PerceptionGraph getRpslperceptiongraphmetamodel_perceptiongraph() {
        return rpslperceptiongraphmetamodel_perceptiongraph;
    }

    public void setRpslperceptiongraphmetamodel_perceptiongraph(rpslPerceptionGraphMetaModel_PerceptionGraph rpslperceptiongraphmetamodel_perceptiongraph) {
        this.rpslperceptiongraphmetamodel_perceptiongraph = rpslperceptiongraphmetamodel_perceptiongraph;
    }

}