





import java.util.List;
import java.util.ArrayList;

public class aadl2_ContainmentPathElement extends Element {

    private String annexName;



    public aadl2_ContainmentPathElement(
        String annexName    ) {
        super(
        );
        this.annexName = annexName;
    }


    public String getAnnexname() {
        return annexName;
    }

    public void setAnnexname(String annexName) {
        this.annexName = annexName;
    }


}