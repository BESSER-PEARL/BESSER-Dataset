





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETLocation  {

    private boolean universal;
    private boolean urgent;
    private String name;





    private ecdarText_ETSpecificationBody ecdartext_etspecificationbody;




    private ecdarText_ETSpecificationBody ecdartext_etspecificationbody;




    private List<ecdarText_ETExpression> ecdartext_etexpressions;


    public ecdarText_ETLocation(
        boolean universal,        boolean urgent,        String name    ) {
        this.universal = universal;
        this.urgent = urgent;
        this.name = name;
        this.ecdartext_etexpressions = new ArrayList<>();
    }

    public ecdarText_ETLocation(
        boolean universal,        boolean urgent,        String name        ArrayList<ecdarText_ETExpression> ecdartext_etexpressions    ) {
        this.universal = universal;
        this.urgent = urgent;
        this.name = name;
        this.ecdartext_etexpressions = ecdartext_etexpressions;
    }

    public boolean getUniversal() {
        return universal;
    }

    public void setUniversal(boolean universal) {
        this.universal = universal;
    }
    public boolean getUrgent() {
        return urgent;
    }

    public void setUrgent(boolean urgent) {
        this.urgent = urgent;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ecdarText_ETSpecificationBody getEcdartext_etspecificationbody() {
        return ecdartext_etspecificationbody;
    }

    public void setEcdartext_etspecificationbody(ecdarText_ETSpecificationBody ecdartext_etspecificationbody) {
        this.ecdartext_etspecificationbody = ecdartext_etspecificationbody;
    }
    public ecdarText_ETSpecificationBody getEcdartext_etspecificationbody() {
        return ecdartext_etspecificationbody;
    }

    public void setEcdartext_etspecificationbody(ecdarText_ETSpecificationBody ecdartext_etspecificationbody) {
        this.ecdartext_etspecificationbody = ecdartext_etspecificationbody;
    }
    public List<ecdarText_ETExpression> getEcdartext_etexpressions() {
        return ecdartext_etexpressions;
    }

    public void addEcdartext_etexpression(Ecdartext_etexpression ecdartext_etexpression) {
        this.ecdartext_etexpressions.add(ecdartext_etexpression);
    }

}