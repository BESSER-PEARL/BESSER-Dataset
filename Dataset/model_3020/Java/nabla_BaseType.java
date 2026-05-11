





import java.util.List;
import java.util.ArrayList;

public class nabla_BaseType  {

    private String primitive;





    private nabla_Function nabla_function;




    private nabla_VarGroupDeclaration nabla_vargroupdeclaration;




    private List<nabla_Expression> nabla_expressions;




    private nabla_Function nabla_function;


    public nabla_BaseType(
        String primitive    ) {
        this.primitive = primitive;
        this.nabla_expressions = new ArrayList<>();
    }

    public nabla_BaseType(
        String primitive        ArrayList<nabla_Expression> nabla_expressions    ) {
        this.primitive = primitive;
        this.nabla_expressions = nabla_expressions;
    }

    public String getPrimitive() {
        return primitive;
    }

    public void setPrimitive(String primitive) {
        this.primitive = primitive;
    }

    public nabla_Function getNabla_function() {
        return nabla_function;
    }

    public void setNabla_function(nabla_Function nabla_function) {
        this.nabla_function = nabla_function;
    }
    public nabla_VarGroupDeclaration getNabla_vargroupdeclaration() {
        return nabla_vargroupdeclaration;
    }

    public void setNabla_vargroupdeclaration(nabla_VarGroupDeclaration nabla_vargroupdeclaration) {
        this.nabla_vargroupdeclaration = nabla_vargroupdeclaration;
    }
    public List<nabla_Expression> getNabla_expressions() {
        return nabla_expressions;
    }

    public void addNabla_expression(Nabla_expression nabla_expression) {
        this.nabla_expressions.add(nabla_expression);
    }
    public nabla_Function getNabla_function() {
        return nabla_function;
    }

    public void setNabla_function(nabla_Function nabla_function) {
        this.nabla_function = nabla_function;
    }

}