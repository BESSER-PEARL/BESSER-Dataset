





import java.util.List;
import java.util.ArrayList;

public class dom_PropertyValue extends Expression {

    private String segments;
    private boolean classProperty;
    private String name;





    private dom_PropertyAssignment dom_propertyassignment;




    private List<dom_Expression> dom_expressions;


    public dom_PropertyValue(
        String segments,        boolean classProperty,        String name    ) {
        super(
        );
        this.segments = segments;
        this.classProperty = classProperty;
        this.name = name;
        this.dom_expressions = new ArrayList<>();
    }

    public dom_PropertyValue(
        String segments,        boolean classProperty,        String name        ArrayList<dom_Expression> dom_expressions    ) {
        this.segments = segments;
        this.classProperty = classProperty;
        this.name = name;
        this.dom_expressions = dom_expressions;
    }

    public String getSegments() {
        return segments;
    }

    public void setSegments(String segments) {
        this.segments = segments;
    }
    public boolean getClassproperty() {
        return classProperty;
    }

    public void setClassproperty(boolean classProperty) {
        this.classProperty = classProperty;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dom_PropertyAssignment getDom_propertyassignment() {
        return dom_propertyassignment;
    }

    public void setDom_propertyassignment(dom_PropertyAssignment dom_propertyassignment) {
        this.dom_propertyassignment = dom_propertyassignment;
    }
    public List<dom_Expression> getDom_expressions() {
        return dom_expressions;
    }

    public void addDom_expression(Dom_expression dom_expression) {
        this.dom_expressions.add(dom_expression);
    }

}