





import java.util.List;
import java.util.ArrayList;

public class vhdl_FileTypeDefinition extends TypeDefinition {

    private String type;



    public vhdl_FileTypeDefinition(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}