





import java.util.List;
import java.util.ArrayList;

public class smachDSL_StateMachine  {

    private String name;





    private smachDSL_PrimitivePackage smachdsl_primitivepackage;




    private List<smachDSL_ActionClient> smachdsl_actionclients;


    public smachDSL_StateMachine(
        String name    ) {
        this.name = name;
        this.smachdsl_actionclients = new ArrayList<>();
    }

    public smachDSL_StateMachine(
        String name        ArrayList<smachDSL_ActionClient> smachdsl_actionclients    ) {
        this.name = name;
        this.smachdsl_actionclients = smachdsl_actionclients;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smachDSL_PrimitivePackage getSmachdsl_primitivepackage() {
        return smachdsl_primitivepackage;
    }

    public void setSmachdsl_primitivepackage(smachDSL_PrimitivePackage smachdsl_primitivepackage) {
        this.smachdsl_primitivepackage = smachdsl_primitivepackage;
    }
    public List<smachDSL_ActionClient> getSmachdsl_actionclients() {
        return smachdsl_actionclients;
    }

    public void addSmachdsl_actionclient(Smachdsl_actionclient smachdsl_actionclient) {
        this.smachdsl_actionclients.add(smachdsl_actionclient);
    }

}