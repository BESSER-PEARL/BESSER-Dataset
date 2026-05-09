





import java.util.List;
import java.util.ArrayList;

public class myDsl_Operation  {

    private String type;





    private myDsl_Submodule mydsl_submodule;


    public myDsl_Operation(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public myDsl_Submodule getMydsl_submodule() {
        return mydsl_submodule;
    }

    public void setMydsl_submodule(myDsl_Submodule mydsl_submodule) {
        this.mydsl_submodule = mydsl_submodule;
    }

}