





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETLocation  {

    private boolean universal;
    private String name;
    private boolean urgent;





    private List<ecdarText_ETExpression> ecdartext_etexpressions;




    private ecdarText_ETSpecificationBody ecdartext_etspecificationbody;




    private ecdarText_ETSpecificationBody ecdartext_etspecificationbody;


    public ecdarText_ETLocation(
        boolean universal,        String name,        boolean urgent    ) {
        this.universal = universal;
        this.name = name;
        this.urgent = urgent;
        this.ecdartext_etexpressions = new ArrayList<>();
    }

    public ecdarText_ETLocation(
        boolean universal,        String name,        boolean urgent        ArrayList<ecdarText_ETExpression> ecdartext_etexpressions    ) {
        this.universal = universal;
        this.name = name;
        this.urgent = urgent;
        this.ecdartext_etexpressions = ecdartext_etexpressions;
    }

    public boolean getUniversal() {
        return universal;
    }

    public void setUniversal(boolean universal) {
        this.universal = universal;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getUrgent() {
        return urgent;
    }

    public void setUrgent(boolean urgent) {
        this.urgent = urgent;
    }

    public List<ecdarText_ETExpression> getEcdartext_etexpressions() {
        return ecdartext_etexpressions;
    }

    public void addEcdartext_etexpression(Ecdartext_etexpression ecdartext_etexpression) {
        this.ecdartext_etexpressions.add(ecdartext_etexpression);
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

}