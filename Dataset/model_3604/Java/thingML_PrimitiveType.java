





import java.util.List;
import java.util.ArrayList;

public class thingML_PrimitiveType extends Type {

    private String ByteSize;



    public thingML_PrimitiveType(
        String ByteSize    ) {
        super(
        );
        this.ByteSize = ByteSize;
    }


    public String getBytesize() {
        return ByteSize;
    }

    public void setBytesize(String ByteSize) {
        this.ByteSize = ByteSize;
    }


}