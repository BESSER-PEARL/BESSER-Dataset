





import java.util.List;
import java.util.ArrayList;

public class SPL_StructureProperty extends LocatedElement {

    private String name;





    private SPL_TypeExpression spl_typeexpression;


    public SPL_StructureProperty(
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

    public SPL_TypeExpression getSpl_typeexpression() {
        return spl_typeexpression;
    }

    public void setSpl_typeexpression(SPL_TypeExpression spl_typeexpression) {
        this.spl_typeexpression = spl_typeexpression;
    }

}