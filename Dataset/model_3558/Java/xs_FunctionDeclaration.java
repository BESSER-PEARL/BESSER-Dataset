





import java.util.List;
import java.util.ArrayList;

public class xs_FunctionDeclaration extends Declaration {

    private String name;
    private boolean mutable;





    private xs_Block xs_block;


    public xs_FunctionDeclaration(
        String name,        boolean mutable    ) {
        super(
        );
        this.name = name;
        this.mutable = mutable;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMutable() {
        return mutable;
    }

    public void setMutable(boolean mutable) {
        this.mutable = mutable;
    }

    public xs_Block getXs_block() {
        return xs_block;
    }

    public void setXs_block(xs_Block xs_block) {
        this.xs_block = xs_block;
    }

}