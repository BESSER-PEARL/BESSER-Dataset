





import java.util.List;
import java.util.ArrayList;

public class DOM_MethodDeclaration extends BodyDeclaration {

    private String constructor;
    private String extraDimensions;
    private String varargs;





    private DOM_SimpleName dom_simplename;




    private DOM_Block dom_block;




    private List<DOM_TypeParameter> dom_typeparameters;




    private List<DOM_Name> dom_names;




    private List<DOM_SingleVariableDeclaration> dom_singlevariabledeclarations;




    private DOM_Type dom_type;


    public DOM_MethodDeclaration(
        String constructor,        String extraDimensions,        String varargs    ) {
        super(
        );
        this.constructor = constructor;
        this.extraDimensions = extraDimensions;
        this.varargs = varargs;
        this.dom_typeparameters = new ArrayList<>();
        this.dom_names = new ArrayList<>();
        this.dom_singlevariabledeclarations = new ArrayList<>();
    }

    public DOM_MethodDeclaration(
        String constructor,        String extraDimensions,        String varargs        ArrayList<DOM_TypeParameter> dom_typeparameters,        ArrayList<DOM_Name> dom_names,        ArrayList<DOM_SingleVariableDeclaration> dom_singlevariabledeclarations    ) {
        this.constructor = constructor;
        this.extraDimensions = extraDimensions;
        this.varargs = varargs;
        this.dom_typeparameters = dom_typeparameters;
        this.dom_names = dom_names;
        this.dom_singlevariabledeclarations = dom_singlevariabledeclarations;
    }

    public String getConstructor() {
        return constructor;
    }

    public void setConstructor(String constructor) {
        this.constructor = constructor;
    }
    public String getExtradimensions() {
        return extraDimensions;
    }

    public void setExtradimensions(String extraDimensions) {
        this.extraDimensions = extraDimensions;
    }
    public String getVarargs() {
        return varargs;
    }

    public void setVarargs(String varargs) {
        this.varargs = varargs;
    }

    public DOM_SimpleName getDom_simplename() {
        return dom_simplename;
    }

    public void setDom_simplename(DOM_SimpleName dom_simplename) {
        this.dom_simplename = dom_simplename;
    }
    public DOM_Block getDom_block() {
        return dom_block;
    }

    public void setDom_block(DOM_Block dom_block) {
        this.dom_block = dom_block;
    }
    public List<DOM_TypeParameter> getDom_typeparameters() {
        return dom_typeparameters;
    }

    public void addDom_typeparameter(Dom_typeparameter dom_typeparameter) {
        this.dom_typeparameters.add(dom_typeparameter);
    }
    public List<DOM_Name> getDom_names() {
        return dom_names;
    }

    public void addDom_name(Dom_name dom_name) {
        this.dom_names.add(dom_name);
    }
    public List<DOM_SingleVariableDeclaration> getDom_singlevariabledeclarations() {
        return dom_singlevariabledeclarations;
    }

    public void addDom_singlevariabledeclaration(Dom_singlevariabledeclaration dom_singlevariabledeclaration) {
        this.dom_singlevariabledeclarations.add(dom_singlevariabledeclaration);
    }
    public DOM_Type getDom_type() {
        return dom_type;
    }

    public void setDom_type(DOM_Type dom_type) {
        this.dom_type = dom_type;
    }

}