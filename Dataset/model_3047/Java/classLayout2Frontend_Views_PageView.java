





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_Views_PageView  {

    private String name;
    private String layoutType;





    private List<ElementView> elementviews;


    public classLayout2Frontend_Views_PageView(
        String name,        String layoutType    ) {
        this.name = name;
        this.layoutType = layoutType;
        this.elementviews = new ArrayList<>();
    }

    public classLayout2Frontend_Views_PageView(
        String name,        String layoutType        ArrayList<ElementView> elementviews    ) {
        this.name = name;
        this.layoutType = layoutType;
        this.elementviews = elementviews;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLayouttype() {
        return layoutType;
    }

    public void setLayouttype(String layoutType) {
        this.layoutType = layoutType;
    }

    public List<ElementView> getElementviews() {
        return elementviews;
    }

    public void addElementview(Elementview elementview) {
        this.elementviews.add(elementview);
    }

}