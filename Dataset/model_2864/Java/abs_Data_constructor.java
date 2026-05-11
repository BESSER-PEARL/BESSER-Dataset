





import java.util.List;
import java.util.ArrayList;

public class abs_Data_constructor  {

    private String name;





    private abs_DataType_decl abs_datatype_decl;


    public abs_Data_constructor(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public abs_DataType_decl getAbs_datatype_decl() {
        return abs_datatype_decl;
    }

    public void setAbs_datatype_decl(abs_DataType_decl abs_datatype_decl) {
        this.abs_datatype_decl = abs_datatype_decl;
    }

}