





import java.util.List;
import java.util.ArrayList;

public class dbl_ListDimension extends TypedElement {

    private int size;





    private dbl_TypedElement dbl_typedelement;


    public dbl_ListDimension(
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

    public dbl_TypedElement getDbl_typedelement() {
        return dbl_typedelement;
    }

    public void setDbl_typedelement(dbl_TypedElement dbl_typedelement) {
        this.dbl_typedelement = dbl_typedelement;
    }

}