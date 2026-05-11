





import java.util.List;
import java.util.ArrayList;

public class Primitives_Expression extends Instruction {






    private Primitives_Right primitives_right;




    private Primitives_Back primitives_back;




    private Primitives_Left primitives_left;


    public Primitives_Expression(
    ) {
        super(
        );
    }



    public Primitives_Right getPrimitives_right() {
        return primitives_right;
    }

    public void setPrimitives_right(Primitives_Right primitives_right) {
        this.primitives_right = primitives_right;
    }
    public Primitives_Back getPrimitives_back() {
        return primitives_back;
    }

    public void setPrimitives_back(Primitives_Back primitives_back) {
        this.primitives_back = primitives_back;
    }
    public Primitives_Left getPrimitives_left() {
        return primitives_left;
    }

    public void setPrimitives_left(Primitives_Left primitives_left) {
        this.primitives_left = primitives_left;
    }

}