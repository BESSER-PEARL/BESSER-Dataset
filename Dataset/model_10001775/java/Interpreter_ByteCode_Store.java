





import java.util.List;
import java.util.ArrayList;

public class Interpreter_ByteCode_Store  {

    private String id;
    private int offset;
    private int value;



    public Interpreter_ByteCode_Store(
        String id,        int offset,        int value    ) {
        this.id = id;
        this.offset = offset;
        this.value = value;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getOffset() {
        return offset;
    }

    public void setOffset(int offset) {
        this.offset = offset;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}