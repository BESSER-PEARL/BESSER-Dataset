





import java.util.List;
import java.util.ArrayList;

public class henshin_Edge extends ModelElement, GraphElement {

    private String index;
    private String indexConstant;



    public henshin_Edge(
        String index,        String indexConstant    ) {
        super(
        );
        this.index = index;
        this.indexConstant = indexConstant;
    }


    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }
    public String getIndexconstant() {
        return indexConstant;
    }

    public void setIndexconstant(String indexConstant) {
        this.indexConstant = indexConstant;
    }


}