





import java.util.List;
import java.util.ArrayList;

public class TypeB_ListElement  {

    private String nameListElement;





    private List<ElementR> elementrs;




    private List<ElementX> elementxs;




    private Element element;




    private List<Element> elements;


    public TypeB_ListElement(
        String nameListElement    ) {
        this.nameListElement = nameListElement;
        this.elementrs = new ArrayList<>();
        this.elementxs = new ArrayList<>();
        this.elements = new ArrayList<>();
    }

    public TypeB_ListElement(
        String nameListElement        ArrayList<ElementR> elementrs,        ArrayList<ElementX> elementxs,        ArrayList<Element> elements    ) {
        this.nameListElement = nameListElement;
        this.elementrs = elementrs;
        this.elementxs = elementxs;
        this.elements = elements;
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
    public Element getElement() {
        return element;
    }

    public void setElement(Element element) {
        this.element = element;
    }
    public List<Element> getElements() {
        return elements;
    }

    public void addElement(Element element) {
        this.elements.add(element);
    }

}