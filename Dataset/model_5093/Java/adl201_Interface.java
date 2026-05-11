





import java.util.List;
import java.util.ArrayList;

public class adl201_Interface  {

    private String name;
    private String signature;



    public adl201_Interface(
        String name,        String signature    ) {
        this.name = name;
        this.signature = signature;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }


}