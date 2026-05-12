





import java.util.List;
import java.util.ArrayList;

public class core_IndexColumnDef extends DatabaseObjectDef {

    private String name;
    private String ordering;
    private int sequence;





    private core_IndexDef core_indexdef;


    public core_IndexColumnDef(
        String name,        String ordering,        int sequence    ) {
        super(
        );
        this.name = name;
        this.ordering = ordering;
        this.sequence = sequence;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }
    public int getSequence() {
        return sequence;
    }

    public void setSequence(int sequence) {
        this.sequence = sequence;
    }

    public core_IndexDef getCore_indexdef() {
        return core_indexdef;
    }

    public void setCore_indexdef(core_IndexDef core_indexdef) {
        this.core_indexdef = core_indexdef;
    }

}