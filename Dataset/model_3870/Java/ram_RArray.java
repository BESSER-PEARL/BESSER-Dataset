





import java.util.List;
import java.util.ArrayList;

public class ram_RArray extends PrimitiveType {

    private int size;





    private ram_ObjectType ram_objecttype;


    public ram_RArray(
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

    public ram_ObjectType getRam_objecttype() {
        return ram_objecttype;
    }

    public void setRam_objecttype(ram_ObjectType ram_objecttype) {
        this.ram_objecttype = ram_objecttype;
    }

}