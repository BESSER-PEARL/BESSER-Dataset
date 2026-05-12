





import java.util.List;
import java.util.ArrayList;

public class core_IndexColumnDef extends DatabaseObjectDef {

    private String ordering;
    private String name;
    private int sequence;





    private core_IndexDef core_indexdef;


    public core_IndexColumnDef(
        String ordering,        String name,        int sequence    ) {
        super(
        );
        this.ordering = ordering;
        this.name = name;
        this.sequence = sequence;
    }


    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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