





import java.util.List;
import java.util.ArrayList;

public class test_ast_E  {

    private boolean derivedBool;
    private boolean lazyBool;



    public test_ast_E(
        boolean derivedBool,        boolean lazyBool    ) {
        this.derivedBool = derivedBool;
        this.lazyBool = lazyBool;
    }


    public boolean getDerivedbool() {
        return derivedBool;
    }

    public void setDerivedbool(boolean derivedBool) {
        this.derivedBool = derivedBool;
    }
    public boolean getLazybool() {
        return lazyBool;
    }

    public void setLazybool(boolean lazyBool) {
        this.lazyBool = lazyBool;
    }


}