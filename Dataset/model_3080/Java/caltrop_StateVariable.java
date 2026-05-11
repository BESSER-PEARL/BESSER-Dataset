





import java.util.List;
import java.util.ArrayList;

public class caltrop_StateVariable extends Variable {

    private boolean binding;
    private boolean constant;



    public caltrop_StateVariable(
        boolean binding,        boolean constant    ) {
        super(
        );
        this.binding = binding;
        this.constant = constant;
    }


    public boolean getBinding() {
        return binding;
    }

    public void setBinding(boolean binding) {
        this.binding = binding;
    }
    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }


}