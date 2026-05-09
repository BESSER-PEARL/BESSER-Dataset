





import java.util.List;
import java.util.ArrayList;

public class dsl_ExplicitConstructorInvocation  {

    private boolean self;
    private String parent;





    private dsl_MethodOrCtorDeclaration dsl_methodorctordeclaration;




    private dsl_Arguments dsl_arguments;


    public dsl_ExplicitConstructorInvocation(
        boolean self,        String parent    ) {
        this.self = self;
        this.parent = parent;
    }


    public boolean getSelf() {
        return self;
    }

    public void setSelf(boolean self) {
        this.self = self;
    }
    public String getParent() {
        return parent;
    }

    public void setParent(String parent) {
        this.parent = parent;
    }

    public dsl_MethodOrCtorDeclaration getDsl_methodorctordeclaration() {
        return dsl_methodorctordeclaration;
    }

    public void setDsl_methodorctordeclaration(dsl_MethodOrCtorDeclaration dsl_methodorctordeclaration) {
        this.dsl_methodorctordeclaration = dsl_methodorctordeclaration;
    }
    public dsl_Arguments getDsl_arguments() {
        return dsl_arguments;
    }

    public void setDsl_arguments(dsl_Arguments dsl_arguments) {
        this.dsl_arguments = dsl_arguments;
    }

}