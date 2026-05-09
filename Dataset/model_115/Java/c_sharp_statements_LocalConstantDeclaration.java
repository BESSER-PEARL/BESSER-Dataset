





import java.util.List;
import java.util.ArrayList;

public class c_sharp_statements_LocalConstantDeclaration  {






    private List<ConstantDeclarator> constantdeclarators;




    private Type type;


    public c_sharp_statements_LocalConstantDeclaration(
    ) {
        this.constantdeclarators = new ArrayList<>();
    }

    public c_sharp_statements_LocalConstantDeclaration(
        ArrayList<ConstantDeclarator> constantdeclarators    ) {
        this.constantdeclarators = constantdeclarators;
    }


    public List<ConstantDeclarator> getConstantdeclarators() {
        return constantdeclarators;
    }

    public void addConstantdeclarator(Constantdeclarator constantdeclarator) {
        this.constantdeclarators.add(constantdeclarator);
    }
    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

}