





import java.util.List;
import java.util.ArrayList;

public class thingML_PrimitiveType extends Type {

    private int ByteSize;



    public thingML_PrimitiveType(
        int ByteSize    ) {
        super(
        );
        this.ByteSize = ByteSize;
    }


    public int getBytesize() {
        return ByteSize;
    }

    public void setBytesize(int ByteSize) {
        this.ByteSize = ByteSize;
    }


}