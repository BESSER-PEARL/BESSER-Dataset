





import java.util.List;
import java.util.ArrayList;

public class kermeta_behavior_VariableDecl extends Expression {

    private String identifier;





    private behavior_TypeReference behavior_typereference;


    public kermeta_behavior_VariableDecl(
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

    public behavior_TypeReference getBehavior_typereference() {
        return behavior_typereference;
    }

    public void setBehavior_typereference(behavior_TypeReference behavior_typereference) {
        this.behavior_typereference = behavior_typereference;
    }

}