





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_ANSINumberType extends ANSIType {

    private String Descriptor;



    public ORDB4ORA_ANSINumberType(
        String Descriptor    ) {
        super(
        );
        this.Descriptor = Descriptor;
    }


    public String getDescriptor() {
        return Descriptor;
    }

    public void setDescriptor(String Descriptor) {
        this.Descriptor = Descriptor;
    }


}