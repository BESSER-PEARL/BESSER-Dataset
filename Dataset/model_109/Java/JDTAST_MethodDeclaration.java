





import java.util.List;
import java.util.ArrayList;

public class JDTAST_MethodDeclaration extends BodyDeclaration {

    private String varargs;
    private String extraDimensions;
    private String constructor;





    private List<JDTAST_Name> jdtast_names;




    private JDTAST_Block jdtast_block;




    private List<JDTAST_SingleVariableDeclaration> jdtast_singlevariabledeclarations;




    private JDTAST_Type jdtast_type;




    private JDTAST_IMethod jdtast_imethod;




    private List<JDTAST_TypeParameter> jdtast_typeparameters;




    private JDTAST_SimpleName jdtast_simplename;


    public JDTAST_MethodDeclaration(
        String varargs,        String extraDimensions,        String constructor    ) {
        super(
        );
        this.varargs = varargs;
        this.extraDimensions = extraDimensions;
        this.constructor = constructor;
        this.jdtast_names = new ArrayList<>();
        this.jdtast_singlevariabledeclarations = new ArrayList<>();
        this.jdtast_typeparameters = new ArrayList<>();
    }

    public JDTAST_MethodDeclaration(
        String varargs,        String extraDimensions,        String constructor        ArrayList<JDTAST_Name> jdtast_names,        ArrayList<JDTAST_SingleVariableDeclaration> jdtast_singlevariabledeclarations,        ArrayList<JDTAST_TypeParameter> jdtast_typeparameters    ) {
        this.varargs = varargs;
        this.extraDimensions = extraDimensions;
        this.constructor = constructor;
        this.jdtast_names = jdtast_names;
        this.jdtast_singlevariabledeclarations = jdtast_singlevariabledeclarations;
        this.jdtast_typeparameters = jdtast_typeparameters;
    }

    public String getVarargs() {
        return varargs;
    }

    public void setVarargs(String varargs) {
        this.varargs = varargs;
    }
    public String getExtradimensions() {
        return extraDimensions;
    }

    public void setExtradimensions(String extraDimensions) {
        this.extraDimensions = extraDimensions;
    }
    public String getConstructor() {
        return constructor;
    }

    public void setConstructor(String constructor) {
        this.constructor = constructor;
    }

    public List<JDTAST_Name> getJdtast_names() {
        return jdtast_names;
    }

    public void addJdtast_name(Jdtast_name jdtast_name) {
        this.jdtast_names.add(jdtast_name);
    }
    public JDTAST_Block getJdtast_block() {
        return jdtast_block;
    }

    public void setJdtast_block(JDTAST_Block jdtast_block) {
        this.jdtast_block = jdtast_block;
    }
    public List<JDTAST_SingleVariableDeclaration> getJdtast_singlevariabledeclarations() {
        return jdtast_singlevariabledeclarations;
    }

    public void addJdtast_singlevariabledeclaration(Jdtast_singlevariabledeclaration jdtast_singlevariabledeclaration) {
        this.jdtast_singlevariabledeclarations.add(jdtast_singlevariabledeclaration);
    }
    public JDTAST_Type getJdtast_type() {
        return jdtast_type;
    }

    public void setJdtast_type(JDTAST_Type jdtast_type) {
        this.jdtast_type = jdtast_type;
    }
    public JDTAST_IMethod getJdtast_imethod() {
        return jdtast_imethod;
    }

    public void setJdtast_imethod(JDTAST_IMethod jdtast_imethod) {
        this.jdtast_imethod = jdtast_imethod;
    }
    public List<JDTAST_TypeParameter> getJdtast_typeparameters() {
        return jdtast_typeparameters;
    }

    public void addJdtast_typeparameter(Jdtast_typeparameter jdtast_typeparameter) {
        this.jdtast_typeparameters.add(jdtast_typeparameter);
    }
    public JDTAST_SimpleName getJdtast_simplename() {
        return jdtast_simplename;
    }

    public void setJdtast_simplename(JDTAST_SimpleName jdtast_simplename) {
        this.jdtast_simplename = jdtast_simplename;
    }

}