





import java.util.List;
import java.util.ArrayList;

public class alf_AcceptClause  {

    private String name;





    private alf_AcceptStatement alf_acceptstatement;


    public alf_AcceptClause(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public alf_AcceptStatement getAlf_acceptstatement() {
        return alf_acceptstatement;
    }

    public void setAlf_acceptstatement(alf_AcceptStatement alf_acceptstatement) {
        this.alf_acceptstatement = alf_acceptstatement;
    }

}