





import java.util.List;
import java.util.ArrayList;

public class ClockRDL_declarations_RelationInstanceDecl extends NamedDeclaration {

    private String qualifiedName;



    public ClockRDL_declarations_RelationInstanceDecl(
        String qualifiedName    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
    }


    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }


}