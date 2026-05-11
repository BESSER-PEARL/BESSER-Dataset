





import java.util.List;
import java.util.ArrayList;

public class archDSL_Param  {

    private String type;
    private String name;





    private archDSL_SuperMethod archdsl_supermethod;


    public archDSL_Param(
        String type,        String name    ) {
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

    public archDSL_SuperMethod getArchdsl_supermethod() {
        return archdsl_supermethod;
    }

    public void setArchdsl_supermethod(archDSL_SuperMethod archdsl_supermethod) {
        this.archdsl_supermethod = archdsl_supermethod;
    }

}