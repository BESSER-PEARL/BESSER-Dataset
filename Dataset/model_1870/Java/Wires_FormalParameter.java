





import java.util.List;
import java.util.ArrayList;

public class Wires_FormalParameter extends Type {

    private String typeName;





    private Wires_DataType wires_datatype;


    public Wires_FormalParameter(
        String typeName    ) {
        super(
        );
        this.typeName = typeName;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }

    public Wires_DataType getWires_datatype() {
        return wires_datatype;
    }

    public void setWires_datatype(Wires_DataType wires_datatype) {
        this.wires_datatype = wires_datatype;
    }

}