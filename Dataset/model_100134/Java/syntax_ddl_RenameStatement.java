





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_RenameStatement extends DefinitionStatement {

    private String system;
    private String newName;
    private String target;



    public syntax_ddl_RenameStatement(
        String system,        String newName,        String target    ) {
        super(
        );
        this.system = system;
        this.newName = newName;
        this.target = target;
    }


    public String getSystem() {
        return system;
    }

    public void setSystem(String system) {
        this.system = system;
    }
    public String getNewname() {
        return newName;
    }

    public void setNewname(String newName) {
        this.newName = newName;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }


}