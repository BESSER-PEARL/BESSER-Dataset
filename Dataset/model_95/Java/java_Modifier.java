





import java.util.List;
import java.util.ArrayList;

public class java_Modifier extends ASTNode {

    private String visibility;
    private boolean static;
    private String inheritance;



    public java_Modifier(
        String visibility,        boolean static,        String inheritance    ) {
        super(
        );
        this.visibility = visibility;
        this.static = static;
        this.inheritance = inheritance;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
    }


}