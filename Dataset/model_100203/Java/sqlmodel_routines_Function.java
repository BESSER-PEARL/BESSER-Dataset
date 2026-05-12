





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_routines_Function extends Routine {

    private String transformGroup;
    private boolean nullCall;
    private boolean typePreserving;
    private boolean mutator;
    private boolean static;



    public sqlmodel_routines_Function(
        String transformGroup,        boolean nullCall,        boolean typePreserving,        boolean mutator,        boolean static    ) {
        super(
        );
        this.transformGroup = transformGroup;
        this.nullCall = nullCall;
        this.typePreserving = typePreserving;
        this.mutator = mutator;
        this.static = static;
    }


    public String getTransformgroup() {
        return transformGroup;
    }

    public void setTransformgroup(String transformGroup) {
        this.transformGroup = transformGroup;
    }
    public boolean getNullcall() {
        return nullCall;
    }

    public void setNullcall(boolean nullCall) {
        this.nullCall = nullCall;
    }
    public boolean getTypepreserving() {
        return typePreserving;
    }

    public void setTypepreserving(boolean typePreserving) {
        this.typePreserving = typePreserving;
    }
    public boolean getMutator() {
        return mutator;
    }

    public void setMutator(boolean mutator) {
        this.mutator = mutator;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }


}