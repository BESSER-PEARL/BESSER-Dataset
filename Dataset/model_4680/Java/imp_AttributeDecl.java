





import java.util.List;
import java.util.ArrayList;

public class imp_AttributeDecl extends Member {

    private String name;





    private imp_Class imp_class;


    public imp_AttributeDecl(
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

    public imp_Class getImp_class() {
        return imp_class;
    }

    public void setImp_class(imp_Class imp_class) {
        this.imp_class = imp_class;
    }

}