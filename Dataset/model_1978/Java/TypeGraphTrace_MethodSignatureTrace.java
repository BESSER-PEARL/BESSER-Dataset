





import java.util.List;
import java.util.ArrayList;

public class TypeGraphTrace_MethodSignatureTrace  {

    private String signatureString;





    private TypeGraphTrace_TMethodSignature typegraphtrace_tmethodsignature;




    private TypeGraphTrace_Trace typegraphtrace_trace;


    public TypeGraphTrace_MethodSignatureTrace(
        String signatureString    ) {
        this.signatureString = signatureString;
    }


    public String getSignaturestring() {
        return signatureString;
    }

    public void setSignaturestring(String signatureString) {
        this.signatureString = signatureString;
    }

    public TypeGraphTrace_TMethodSignature getTypegraphtrace_tmethodsignature() {
        return typegraphtrace_tmethodsignature;
    }

    public void setTypegraphtrace_tmethodsignature(TypeGraphTrace_TMethodSignature typegraphtrace_tmethodsignature) {
        this.typegraphtrace_tmethodsignature = typegraphtrace_tmethodsignature;
    }
    public TypeGraphTrace_Trace getTypegraphtrace_trace() {
        return typegraphtrace_trace;
    }

    public void setTypegraphtrace_trace(TypeGraphTrace_Trace typegraphtrace_trace) {
        this.typegraphtrace_trace = typegraphtrace_trace;
    }

}