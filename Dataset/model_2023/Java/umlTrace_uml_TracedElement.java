





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedElement extends TracedEModelElement {






    private List<uml_TracedComment> uml_tracedcomments;




    private uml_TracedElement uml_tracedelement;




    private List<uml_TracedElement> uml_tracedelements;




    private List<Element_semanticVisitor_Value> element_semanticvisitor_values;


    public umlTrace_uml_TracedElement(
    ) {
        super(
        );
        this.uml_tracedcomments = new ArrayList<>();
        this.uml_tracedelements = new ArrayList<>();
        this.element_semanticvisitor_values = new ArrayList<>();
    }

    public umlTrace_uml_TracedElement(
        ArrayList<uml_TracedComment> uml_tracedcomments,        ArrayList<uml_TracedElement> uml_tracedelements,        ArrayList<Element_semanticVisitor_Value> element_semanticvisitor_values    ) {
        this.uml_tracedcomments = uml_tracedcomments;
        this.uml_tracedelements = uml_tracedelements;
        this.element_semanticvisitor_values = element_semanticvisitor_values;
    }


    public List<uml_TracedComment> getUml_tracedcomments() {
        return uml_tracedcomments;
    }

    public void addUml_tracedcomment(Uml_tracedcomment uml_tracedcomment) {
        this.uml_tracedcomments.add(uml_tracedcomment);
    }
    public uml_TracedElement getUml_tracedelement() {
        return uml_tracedelement;
    }

    public void setUml_tracedelement(uml_TracedElement uml_tracedelement) {
        this.uml_tracedelement = uml_tracedelement;
    }
    public List<uml_TracedElement> getUml_tracedelements() {
        return uml_tracedelements;
    }

    public void addUml_tracedelement(Uml_tracedelement uml_tracedelement) {
        this.uml_tracedelements.add(uml_tracedelement);
    }
    public List<Element_semanticVisitor_Value> getElement_semanticvisitor_values() {
        return element_semanticvisitor_values;
    }

    public void addElement_semanticvisitor_value(Element_semanticvisitor_value element_semanticvisitor_value) {
        this.element_semanticvisitor_values.add(element_semanticvisitor_value);
    }

}