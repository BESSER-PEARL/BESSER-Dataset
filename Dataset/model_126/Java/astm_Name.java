





import java.util.List;
import java.util.ArrayList;

public class astm_Name extends OtherSyntaxObject {

    private String nameString;



    public astm_Name(
        String nameString    ) {
        super(
        );
        this.nameString = nameString;
    }


    public String getNamestring() {
        return nameString;
    }

    public void setNamestring(String nameString) {
        this.nameString = nameString;
    }


}