





import java.util.List;
import java.util.ArrayList;

public class myDsl_LogicStructure  {

    private String name;





    private myDsl_LogicContent mydsl_logiccontent;


    public myDsl_LogicStructure(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_LogicContent getMydsl_logiccontent() {
        return mydsl_logiccontent;
    }

    public void setMydsl_logiccontent(myDsl_LogicContent mydsl_logiccontent) {
        this.mydsl_logiccontent = mydsl_logiccontent;
    }

}