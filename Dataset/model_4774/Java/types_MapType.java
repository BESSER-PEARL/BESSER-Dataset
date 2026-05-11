





import java.util.List;
import java.util.ArrayList;

public class types_MapType extends DeclarationTypeReference, Type {

    private int size;



    public types_MapType(
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