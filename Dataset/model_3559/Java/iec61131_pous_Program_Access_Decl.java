





import java.util.List;
import java.util.ArrayList;

public class iec61131_pous_Program_Access_Decl  {

    private String direction;





    private Non_Generic_Type_Name non_generic_type_name;


    public iec61131_pous_Program_Access_Decl(
        String direction    ) {
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public Non_Generic_Type_Name getNon_generic_type_name() {
        return non_generic_type_name;
    }

    public void setNon_generic_type_name(Non_Generic_Type_Name non_generic_type_name) {
        this.non_generic_type_name = non_generic_type_name;
    }

}