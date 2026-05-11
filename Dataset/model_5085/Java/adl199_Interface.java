





import java.util.List;
import java.util.ArrayList;

public class adl199_Interface  {

    private String signature;
    private String name;



    public adl199_Interface(
        String signature,        String name    ) {
        this.signature = signature;
        this.name = name;
    }


    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}