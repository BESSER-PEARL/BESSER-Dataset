





import java.util.List;
import java.util.ArrayList;

public class simplejava_Method  {

    private boolean static;
    private String name;





    private simplejava_ClassDeclaration simplejava_classdeclaration;


    public simplejava_Method(
        boolean static,        String name    ) {
        this.static = static;
        this.name = name;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simplejava_ClassDeclaration getSimplejava_classdeclaration() {
        return simplejava_classdeclaration;
    }

    public void setSimplejava_classdeclaration(simplejava_ClassDeclaration simplejava_classdeclaration) {
        this.simplejava_classdeclaration = simplejava_classdeclaration;
    }

}