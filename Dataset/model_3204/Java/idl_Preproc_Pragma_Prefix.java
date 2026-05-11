





import java.util.List;
import java.util.ArrayList;

public class idl_Preproc_Pragma_Prefix extends Preproc_Pragma {

    private String value;



    public idl_Preproc_Pragma_Prefix(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}