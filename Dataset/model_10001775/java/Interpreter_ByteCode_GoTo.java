





import java.util.List;
import java.util.ArrayList;

public class Interpreter_ByteCode_GoTo  {

    private String label;
    private int address;



    public Interpreter_ByteCode_GoTo(
        String label,        int address    ) {
        this.label = label;
        this.address = address;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public int getAddress() {
        return address;
    }

    public void setAddress(int address) {
        this.address = address;
    }


}