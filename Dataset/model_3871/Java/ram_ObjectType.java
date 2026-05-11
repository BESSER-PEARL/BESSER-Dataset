





import java.util.List;
import java.util.ArrayList;

public class ram_ObjectType extends Type, MappableElement {






    private ram_Reference ram_reference;




    private ram_RCollection ram_rcollection;


    public ram_ObjectType(
    ) {
        super(
        );
    }



    public ram_Reference getRam_reference() {
        return ram_reference;
    }

    public void setRam_reference(ram_Reference ram_reference) {
        this.ram_reference = ram_reference;
    }
    public ram_RCollection getRam_rcollection() {
        return ram_rcollection;
    }

    public void setRam_rcollection(ram_RCollection ram_rcollection) {
        this.ram_rcollection = ram_rcollection;
    }

}