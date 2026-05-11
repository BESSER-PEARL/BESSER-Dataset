





import java.util.List;
import java.util.ArrayList;

public class ir_ItemIdValueIterator extends ItemIdValue {

    private int shift;





    private ir_Iterator ir_iterator;


    public ir_ItemIdValueIterator(
        int shift    ) {
        super(
        );
        this.shift = shift;
    }


    public int getShift() {
        return shift;
    }

    public void setShift(int shift) {
        this.shift = shift;
    }

    public ir_Iterator getIr_iterator() {
        return ir_iterator;
    }

    public void setIr_iterator(ir_Iterator ir_iterator) {
        this.ir_iterator = ir_iterator;
    }

}