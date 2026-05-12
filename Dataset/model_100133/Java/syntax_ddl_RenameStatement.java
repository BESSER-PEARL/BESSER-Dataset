





import java.util.List;
import java.util.ArrayList;

public class syntax_ddl_RenameStatement extends DefinitionStatement {

    private String newName;
    private String target;
    private String system;



    public syntax_ddl_RenameStatement(
        String newName,        String target,        String system    ) {
        super(
        );
        this.newName = newName;
        this.target = target;
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
    public String getSystem() {
        return system;
    }

    public void setSystem(String system) {
        this.system = system;
    }


}