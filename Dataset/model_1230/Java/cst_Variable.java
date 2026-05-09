





import java.util.List;
import java.util.ArrayList;

public class cst_Variable extends CSTNode {

    private String type;
    private String name;





    private cst_InitSection cst_initsection;


    public cst_Variable(
        String type,        String name    ) {
        super(
        );
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cst_InitSection getCst_initsection() {
        return cst_initsection;
    }

    public void setCst_initsection(cst_InitSection cst_initsection) {
        this.cst_initsection = cst_initsection;
    }

}