





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_MethodDeclaration extends BodyDeclaration {

    private String extraDimensions;
    private String constructor;
    private String varargs;





    private Block block;




    private List<SingleVariableDeclaration> singlevariabledeclarations;


    public JavaAbstractSyntax_MethodDeclaration(
        String extraDimensions,        String constructor,        String varargs    ) {
        super(
        );
        this.extraDimensions = extraDimensions;
        this.constructor = constructor;
        this.varargs = varargs;
        this.singlevariabledeclarations = new ArrayList<>();
    }

    public JavaAbstractSyntax_MethodDeclaration(
        String extraDimensions,        String constructor,        String varargs        ArrayList<SingleVariableDeclaration> singlevariabledeclarations    ) {
        this.extraDimensions = extraDimensions;
        this.constructor = constructor;
        this.varargs = varargs;
        this.singlevariabledeclarations = singlevariabledeclarations;
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
    public String getVarargs() {
        return varargs;
    }

    public void setVarargs(String varargs) {
        this.varargs = varargs;
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