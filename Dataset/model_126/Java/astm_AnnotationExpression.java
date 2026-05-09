





import java.util.List;
import java.util.ArrayList;

public class astm_AnnotationExpression extends Expression {






    private astm_TypeReference astm_typereference;




    private List<astm_Expression> astm_expressions;




    private astm_GASTMSyntaxObject astm_gastmsyntaxobject;


    public astm_AnnotationExpression(
    ) {
        super(
        );
        this.astm_expressions = new ArrayList<>();
    }

    public astm_AnnotationExpression(
        ArrayList<astm_Expression> astm_expressions    ) {
        this.astm_expressions = astm_expressions;
    }


    public astm_TypeReference getAstm_typereference() {
        return astm_typereference;
    }

    public void setAstm_typereference(astm_TypeReference astm_typereference) {
        this.astm_typereference = astm_typereference;
    }
    public List<astm_Expression> getAstm_expressions() {
        return astm_expressions;
    }

    public void addAstm_expression(Astm_expression astm_expression) {
        this.astm_expressions.add(astm_expression);
    }
    public astm_GASTMSyntaxObject getAstm_gastmsyntaxobject() {
        return astm_gastmsyntaxobject;
    }

    public void setAstm_gastmsyntaxobject(astm_GASTMSyntaxObject astm_gastmsyntaxobject) {
        this.astm_gastmsyntaxobject = astm_gastmsyntaxobject;
    }

}