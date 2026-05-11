





import java.util.List;
import java.util.ArrayList;

public class types_ArrayType extends Type {

    private int arraySelector;



    public types_ArrayType(
        int arraySelector    ) {
        super(
        );
        this.arraySelector = arraySelector;
    }


    public int getArrayselector() {
        return arraySelector;
    }

    public void setArrayselector(int arraySelector) {
        this.arraySelector = arraySelector;
    }


}