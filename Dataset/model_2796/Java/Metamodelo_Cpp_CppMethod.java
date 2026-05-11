





import java.util.List;
import java.util.ArrayList;

public class Metamodelo_Cpp_CppMethod extends CppTypedElement, CppMemberFunction {

    private boolean isVirtual;
    private boolean isPureVirtual;
    private boolean isFinal;
    private boolean isConst;



    public Metamodelo_Cpp_CppMethod(
        boolean isVirtual,        boolean isPureVirtual,        boolean isFinal,        boolean isConst    ) {
        super(
        );
        this.isVirtual = isVirtual;
        this.isPureVirtual = isPureVirtual;
        this.isFinal = isFinal;
        this.isConst = isConst;
    }


    public boolean getIsvirtual() {
        return isVirtual;
    }

    public void setIsvirtual(boolean isVirtual) {
        this.isVirtual = isVirtual;
    }
    public boolean getIspurevirtual() {
        return isPureVirtual;
    }

    public void setIspurevirtual(boolean isPureVirtual) {
        this.isPureVirtual = isPureVirtual;
    }
    public boolean getIsfinal() {
        return isFinal;
    }

    public void setIsfinal(boolean isFinal) {
        this.isFinal = isFinal;
    }
    public boolean getIsconst() {
        return isConst;
    }

    public void setIsconst(boolean isConst) {
        this.isConst = isConst;
    }


}