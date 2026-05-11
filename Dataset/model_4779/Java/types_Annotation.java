





import java.util.List;
import java.util.ArrayList;

public class types_Annotation  {






    private List<types_Expression> types_expressions;




    private types_AnnotationType types_annotationtype;


    public types_Annotation(
    ) {
        this.types_expressions = new ArrayList<>();
    }

    public types_Annotation(
        ArrayList<types_Expression> types_expressions    ) {
        this.types_expressions = types_expressions;
    }


    public List<types_Expression> getTypes_expressions() {
        return types_expressions;
    }

    public void addTypes_expression(Types_expression types_expression) {
        this.types_expressions.add(types_expression);
    }
    public types_AnnotationType getTypes_annotationtype() {
        return types_annotationtype;
    }

    public void setTypes_annotationtype(types_AnnotationType types_annotationtype) {
        this.types_annotationtype = types_annotationtype;
    }

}