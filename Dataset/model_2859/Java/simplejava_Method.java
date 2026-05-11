





import java.util.List;
import java.util.ArrayList;

public class simplejava_Method  {

    private String name;
    private boolean static;





    private simplejava_MethodBlock simplejava_methodblock;




    private simplejava_MethodCall simplejava_methodcall;




    private simplejava_ClassDeclaration simplejava_classdeclaration;


    public simplejava_Method(
        String name,        boolean static    ) {
        this.name = name;
        this.static = static;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public simplejava_MethodBlock getSimplejava_methodblock() {
        return simplejava_methodblock;
    }

    public void setSimplejava_methodblock(simplejava_MethodBlock simplejava_methodblock) {
        this.simplejava_methodblock = simplejava_methodblock;
    }
    public simplejava_MethodCall getSimplejava_methodcall() {
        return simplejava_methodcall;
    }

    public void setSimplejava_methodcall(simplejava_MethodCall simplejava_methodcall) {
        this.simplejava_methodcall = simplejava_methodcall;
    }
    public simplejava_ClassDeclaration getSimplejava_classdeclaration() {
        return simplejava_classdeclaration;
    }

    public void setSimplejava_classdeclaration(simplejava_ClassDeclaration simplejava_classdeclaration) {
        this.simplejava_classdeclaration = simplejava_classdeclaration;
    }

}