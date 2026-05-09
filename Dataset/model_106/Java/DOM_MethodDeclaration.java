





import java.util.List;
import java.util.ArrayList;

public class DOM_MethodDeclaration extends BodyDeclaration {

    private String constructor;
    private String extraDimensions;
    private String varargs;





    private IMethod imethod;




    private Block block;




    private List<SingleVariableDeclaration> singlevariabledeclarations;


    public DOM_MethodDeclaration(
        String constructor,        String extraDimensions,        String varargs    ) {
        super(
        );
        this.constructor = constructor;
        this.extraDimensions = extraDimensions;
        this.varargs = varargs;
        this.singlevariabledeclarations = new ArrayList<>();
    }

    public DOM_MethodDeclaration(
        String constructor,        String extraDimensions,        String varargs        ArrayList<SingleVariableDeclaration> singlevariabledeclarations    ) {
        this.constructor = constructor;
        this.extraDimensions = extraDimensions;
        this.varargs = varargs;
        this.singlevariabledeclarations = singlevariabledeclarations;
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
    public List<SingleVariableDeclaration> getSinglevariabledeclarations() {
        return singlevariabledeclarations;
    }

    public void addSinglevariabledeclaration(Singlevariabledeclaration singlevariabledeclaration) {
        this.singlevariabledeclarations.add(singlevariabledeclaration);
    }

}