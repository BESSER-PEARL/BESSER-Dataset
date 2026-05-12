





import java.util.List;
import java.util.ArrayList;

public class Interpreter_ByteCode_Load  {

    private String id;
    private int offset;



    public Interpreter_ByteCode_Load(
        String id,        int offset    ) {
        this.id = id;
        this.offset = offset;
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


}