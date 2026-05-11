





import java.util.List;
import java.util.ArrayList;

public class adb_Mode  {

    private boolean out;
    private boolean in_;





    private adb_ParameterSpecification adb_parameterspecification;




    private adb_FormalObjectDeclaration adb_formalobjectdeclaration;


    public adb_Mode(
        boolean out,        boolean in_    ) {
        this.out = out;
        this.in_ = in_;
    }


    public boolean getOut() {
        return out;
    }

    public void setOut(boolean out) {
        this.out = out;
    }
    public boolean getIn_() {
        return in_;
    }

    public void setIn_(boolean in_) {
        this.in_ = in_;
    }

    public adb_ParameterSpecification getAdb_parameterspecification() {
        return adb_parameterspecification;
    }

    public void setAdb_parameterspecification(adb_ParameterSpecification adb_parameterspecification) {
        this.adb_parameterspecification = adb_parameterspecification;
    }
    public adb_FormalObjectDeclaration getAdb_formalobjectdeclaration() {
        return adb_formalobjectdeclaration;
    }

    public void setAdb_formalobjectdeclaration(adb_FormalObjectDeclaration adb_formalobjectdeclaration) {
        this.adb_formalobjectdeclaration = adb_formalobjectdeclaration;
    }

}