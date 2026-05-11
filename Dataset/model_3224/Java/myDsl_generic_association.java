





import java.util.List;
import java.util.ArrayList;

public class myDsl_generic_association  {

    private String default;





    private myDsl_generic_assoc_list mydsl_generic_assoc_list;


    public myDsl_generic_association(
        String default    ) {
        this.default = default;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public myDsl_generic_assoc_list getMydsl_generic_assoc_list() {
        return mydsl_generic_assoc_list;
    }

    public void setMydsl_generic_assoc_list(myDsl_generic_assoc_list mydsl_generic_assoc_list) {
        this.mydsl_generic_assoc_list = mydsl_generic_assoc_list;
    }

}