





import java.util.List;
import java.util.ArrayList;

public class jointPackage_Ecore2Maude_TrgOperation extends TrgModElement {

    private String atts;
    private String name;



    public jointPackage_Ecore2Maude_TrgOperation(
        String atts,        String name    ) {
        super(
        );
        this.atts = atts;
        this.name = name;
    }


    public String getAtts() {
        return atts;
    }

    public void setAtts(String atts) {
        this.atts = atts;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}