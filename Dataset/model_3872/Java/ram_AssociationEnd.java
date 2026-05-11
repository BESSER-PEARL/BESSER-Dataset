





import java.util.List;
import java.util.ArrayList;

public class ram_AssociationEnd extends Property {

    private boolean navigable;





    private ram_Class ram_class;




    private ram_Association ram_association;




    private ram_Class ram_class;




    private ram_Association ram_association;


    public ram_AssociationEnd(
        boolean navigable    ) {
        super(
        );
        this.navigable = navigable;
    }


    public boolean getNavigable() {
        return navigable;
    }

    public void setNavigable(boolean navigable) {
        this.navigable = navigable;
    }

    public ram_Class getRam_class() {
        return ram_class;
    }

    public void setRam_class(ram_Class ram_class) {
        this.ram_class = ram_class;
    }
    public ram_Association getRam_association() {
        return ram_association;
    }

    public void setRam_association(ram_Association ram_association) {
        this.ram_association = ram_association;
    }
    public ram_Class getRam_class() {
        return ram_class;
    }

    public void setRam_class(ram_Class ram_class) {
        this.ram_class = ram_class;
    }
    public ram_Association getRam_association() {
        return ram_association;
    }

    public void setRam_association(ram_Association ram_association) {
        this.ram_association = ram_association;
    }

}