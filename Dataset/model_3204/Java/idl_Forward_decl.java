





import java.util.List;
import java.util.ArrayList;

public class idl_Forward_decl extends Interface_or_Forward_Decl {

    private String name;



    public idl_Forward_decl(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}