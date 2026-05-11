





import java.util.List;
import java.util.ArrayList;

public class mm_ops_AddSequence extends ModelOperation {

    private int startValue;
    private String owningSchemaName;
    private String name;



    public mm_ops_AddSequence(
        int startValue,        String owningSchemaName,        String name    ) {
        super(
        );
        this.startValue = startValue;
        this.owningSchemaName = owningSchemaName;
        this.name = name;
    }


    public int getStartvalue() {
        return startValue;
    }

    public void setStartvalue(int startValue) {
        this.startValue = startValue;
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