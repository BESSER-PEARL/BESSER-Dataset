





import java.util.List;
import java.util.ArrayList;

public class alf_AcceptClause  {

    private String name;





    private alf_AcceptStatement alf_acceptstatement;




    private alf_QualifiedNameList alf_qualifiednamelist;




    private alf_AcceptBlock alf_acceptblock;


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
    public alf_QualifiedNameList getAlf_qualifiednamelist() {
        return alf_qualifiednamelist;
    }

    public void setAlf_qualifiednamelist(alf_QualifiedNameList alf_qualifiednamelist) {
        this.alf_qualifiednamelist = alf_qualifiednamelist;
    }
    public alf_AcceptBlock getAlf_acceptblock() {
        return alf_acceptblock;
    }

    public void setAlf_acceptblock(alf_AcceptBlock alf_acceptblock) {
        this.alf_acceptblock = alf_acceptblock;
    }

}