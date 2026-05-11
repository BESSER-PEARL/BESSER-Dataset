





import java.util.List;
import java.util.ArrayList;

public class idl_Preproc_Include extends Preproc {

    private String strValue;



    public idl_Preproc_Include(
        String strValue    ) {
        super(
        );
        this.strValue = strValue;
    }


    public String getStrvalue() {
        return strValue;
    }

    public void setStrvalue(String strValue) {
        this.strValue = strValue;
    }


}