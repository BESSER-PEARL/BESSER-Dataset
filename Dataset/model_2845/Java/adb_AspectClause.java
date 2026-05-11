





import java.util.List;
import java.util.ArrayList;

public class adb_AspectClause extends ProtectedOperationDeclaration, ProtectedOperationItem, ComponentItem, BasicDeclarativeItem, TaskItem {

    private String name;



    public adb_AspectClause(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}