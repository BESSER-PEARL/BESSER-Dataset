





import java.util.List;
import java.util.ArrayList;

public class uma_DiagramElement extends MethodElement {

    private String isVisible;





    private List<uma_Property> uma_propertys;




    private uma_Reference uma_reference;




    private uma_GraphElement uma_graphelement;




    private List<uma_Reference> uma_references;




    private uma_GraphElement uma_graphelement;


    public uma_DiagramElement(
        String isVisible    ) {
        super(
        );
        this.isVisible = isVisible;
        this.uma_propertys = new ArrayList<>();
        this.uma_references = new ArrayList<>();
    }

    public uma_DiagramElement(
        String isVisible        ArrayList<uma_Property> uma_propertys,        ArrayList<uma_Reference> uma_references    ) {
        this.isVisible = isVisible;
        this.uma_propertys = uma_propertys;
        this.uma_references = uma_references;
    }

    public String getIsvisible() {
        return isVisible;
    }

    public void setIsvisible(String isVisible) {
        this.isVisible = isVisible;
    }

    public List<uma_Property> getUma_propertys() {
        return uma_propertys;
    }

    public void addUma_property(Uma_property uma_property) {
        this.uma_propertys.add(uma_property);
    }
    public uma_Reference getUma_reference() {
        return uma_reference;
    }

    public void setUma_reference(uma_Reference uma_reference) {
        this.uma_reference = uma_reference;
    }
    public uma_GraphElement getUma_graphelement() {
        return uma_graphelement;
    }

    public void setUma_graphelement(uma_GraphElement uma_graphelement) {
        this.uma_graphelement = uma_graphelement;
    }
    public List<uma_Reference> getUma_references() {
        return uma_references;
    }

    public void addUma_reference(Uma_reference uma_reference) {
        this.uma_references.add(uma_reference);
    }
    public uma_GraphElement getUma_graphelement() {
        return uma_graphelement;
    }

    public void setUma_graphelement(uma_GraphElement uma_graphelement) {
        this.uma_graphelement = uma_graphelement;
    }

}