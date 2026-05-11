





import java.util.List;
import java.util.ArrayList;

public class types_ArrayTypeSpecifier extends TypeSpecifier {

    private int size;



    public types_ArrayTypeSpecifier(
        int size    ) {
        super(
        );
        this.size = size;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}