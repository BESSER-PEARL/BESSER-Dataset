





import java.util.List;
import java.util.ArrayList;

public class mm_ops_RenameTable extends ModelOperation {

    private String newName;
    private String owningSchemaName;
    private String name;



    public mm_ops_RenameTable(
        String newName,        String owningSchemaName,        String name    ) {
        super(
        );
        this.newName = newName;
        this.owningSchemaName = owningSchemaName;
        this.name = name;
    }


    public String getNewname() {
        return newName;
    }

    public void setNewname(String newName) {
        this.newName = newName;
    }
    public String getOwningschemaname() {
        return owningSchemaName;
    }

    public void setOwningschemaname(String owningSchemaName) {
        this.owningSchemaName = owningSchemaName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}