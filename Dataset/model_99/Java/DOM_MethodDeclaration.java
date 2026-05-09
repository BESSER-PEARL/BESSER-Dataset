





import java.util.List;
import java.util.ArrayList;

public class DOM_MethodDeclaration extends BodyDeclaration {

    private String constructor;
    private String varargs;
    private String extraDimensions;





    private List<SingleVariableDeclaration> singlevariabledeclarations;




    private IMethod imethod;




    private Block block;


    public DOM_MethodDeclaration(
        String constructor,        String varargs,        String extraDimensions    ) {
        super(
        );
        this.constructor = constructor;
        this.varargs = varargs;
        this.extraDimensions = extraDimensions;
        this.singlevariabledeclarations = new ArrayList<>();
    }

    public DOM_MethodDeclaration(
        String constructor,        String varargs,        String extraDimensions        ArrayList<SingleVariableDeclaration> singlevariabledeclarations    ) {
        this.constructor = constructor;
        this.varargs = varargs;
        this.extraDimensions = extraDimensions;
        this.singlevariabledeclarations = singlevariabledeclarations;
    }

    public String getConstructor() {
        return constructor;
    }

    public void setConstructor(String constructor) {
        this.constructor = constructor;
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

    public List<SingleVariableDeclaration> getSinglevariabledeclarations() {
        return singlevariabledeclarations;
    }

    public void addSinglevariabledeclaration(Singlevariabledeclaration singlevariabledeclaration) {
        this.singlevariabledeclarations.add(singlevariabledeclaration);
    }
    public IMethod getImethod() {
        return imethod;
    }

    public void setImethod(IMethod imethod) {
        this.imethod = imethod;
    }
    public Block getBlock() {
        return block;
    }

    public void setBlock(Block block) {
        this.block = block;
    }

}