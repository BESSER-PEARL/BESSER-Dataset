





import java.util.List;
import java.util.ArrayList;

public class dslComponent_DocumElt  {

    private String name;
    private String desc;



    public dslComponent_DocumElt(
        String name,        String desc    ) {
        this.name = name;
        this.desc = desc;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }


}