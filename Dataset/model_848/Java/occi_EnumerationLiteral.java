





import java.util.List;
import java.util.ArrayList;

public class occi_EnumerationLiteral  {

    private String name;
    private String documentation;





    private occi_State occi_state;


    public occi_EnumerationLiteral(
        String name,        String documentation    ) {
        this.name = name;
        this.documentation = documentation;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
    }

    public occi_State getOcci_state() {
        return occi_state;
    }

    public void setOcci_state(occi_State occi_state) {
        this.occi_state = occi_state;
    }

}