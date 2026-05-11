





import java.util.List;
import java.util.ArrayList;

public class TypeB_ListElement  {

    private String nameListElement;





    private List<ElementR> elementrs;




    private List<ElementX> elementxs;


    public TypeB_ListElement(
        String nameListElement    ) {
        this.nameListElement = nameListElement;
        this.elementrs = new ArrayList<>();
        this.elementxs = new ArrayList<>();
    }

    public TypeB_ListElement(
        String nameListElement        ArrayList<ElementR> elementrs,        ArrayList<ElementX> elementxs    ) {
        this.nameListElement = nameListElement;
        this.elementrs = elementrs;
        this.elementxs = elementxs;
    }

    public String getNamelistelement() {
        return nameListElement;
    }

    public void setNamelistelement(String nameListElement) {
        this.nameListElement = nameListElement;
    }

    public List<ElementR> getElementrs() {
        return elementrs;
    }

    public void addElementr(Elementr elementr) {
        this.elementrs.add(elementr);
    }
    public List<ElementX> getElementxs() {
        return elementxs;
    }

    public void addElementx(Elementx elementx) {
        this.elementxs.add(elementx);
    }

}