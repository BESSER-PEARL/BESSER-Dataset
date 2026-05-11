





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_Constraint extends Declaration {

    private String name;





    private OPLmetamodel_Assertion oplmetamodel_assertion;


    public OPLmetamodel_Constraint(
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

    public OPLmetamodel_Assertion getOplmetamodel_assertion() {
        return oplmetamodel_assertion;
    }

    public void setOplmetamodel_assertion(OPLmetamodel_Assertion oplmetamodel_assertion) {
        this.oplmetamodel_assertion = oplmetamodel_assertion;
    }

}