





import java.util.List;
import java.util.ArrayList;

public class edd_TreeElement  {

    private String name;
    private String index;





    private edd_Block edd_block;




    private edd_TreeElement edd_treeelement;


    public edd_TreeElement(
        String name,        String index    ) {
        this.name = name;
        this.index = index;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }

    public edd_Block getEdd_block() {
        return edd_block;
    }

    public void setEdd_block(edd_Block edd_block) {
        this.edd_block = edd_block;
    }
    public edd_TreeElement getEdd_treeelement() {
        return edd_treeelement;
    }

    public void setEdd_treeelement(edd_TreeElement edd_treeelement) {
        this.edd_treeelement = edd_treeelement;
    }

}