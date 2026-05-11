





import java.util.List;
import java.util.ArrayList;

public class adfg_Port  {

    private String type;
    private String name;
    private String sequence;



    public adfg_Port(
        String type,        String name,        String sequence    ) {
        this.type = type;
        this.name = name;
        this.sequence = sequence;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSequence() {
        return sequence;
    }

    public void setSequence(String sequence) {
        this.sequence = sequence;
    }


}