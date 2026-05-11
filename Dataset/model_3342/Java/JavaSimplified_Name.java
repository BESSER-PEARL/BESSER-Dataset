





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_Name extends Expression {

    private String identifier;





    private JavaSimplified_NamedElement javasimplified_namedelement;


    public JavaSimplified_Name(
        String identifier    ) {
        super(
        );
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public JavaSimplified_NamedElement getJavasimplified_namedelement() {
        return javasimplified_namedelement;
    }

    public void setJavasimplified_namedelement(JavaSimplified_NamedElement javasimplified_namedelement) {
        this.javasimplified_namedelement = javasimplified_namedelement;
    }

}