





import java.util.List;
import java.util.ArrayList;

public class simplejava_Parameter  {

    private String name;





    private simplejava_MethodCall simplejava_methodcall;




    private simplejava_Assignment simplejava_assignment;




    private simplejava_ClassDeclaration simplejava_classdeclaration;


    public simplejava_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public simplejava_MethodCall getSimplejava_methodcall() {
        return simplejava_methodcall;
    }

    public void setSimplejava_methodcall(simplejava_MethodCall simplejava_methodcall) {
        this.simplejava_methodcall = simplejava_methodcall;
    }
    public simplejava_Assignment getSimplejava_assignment() {
        return simplejava_assignment;
    }

    public void setSimplejava_assignment(simplejava_Assignment simplejava_assignment) {
        this.simplejava_assignment = simplejava_assignment;
    }
    public simplejava_ClassDeclaration getSimplejava_classdeclaration() {
        return simplejava_classdeclaration;
    }

    public void setSimplejava_classdeclaration(simplejava_ClassDeclaration simplejava_classdeclaration) {
        this.simplejava_classdeclaration = simplejava_classdeclaration;
    }

}