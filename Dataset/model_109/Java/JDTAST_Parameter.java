





import java.util.List;
import java.util.ArrayList;

public class JDTAST_Parameter  {

    private String name;
    private String type;





    private JDTAST_IMethod jdtast_imethod;


    public JDTAST_Parameter(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public JDTAST_IMethod getJdtast_imethod() {
        return jdtast_imethod;
    }

    public void setJdtast_imethod(JDTAST_IMethod jdtast_imethod) {
        this.jdtast_imethod = jdtast_imethod;
    }

}