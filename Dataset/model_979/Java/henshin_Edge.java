





import java.util.List;
import java.util.ArrayList;

public class henshin_Edge extends ModelElement, GraphElement {

    private String indexConstant;
    private String index;



    public henshin_Edge(
        String indexConstant,        String index    ) {
        super(
        );
        this.indexConstant = indexConstant;
        this.index = index;
    }


    public String getIndexconstant() {
        return indexConstant;
    }

    public void setIndexconstant(String indexConstant) {
        this.indexConstant = indexConstant;
    }
    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }


}