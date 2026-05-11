





import java.util.List;
import java.util.ArrayList;

public class myDsl_IdentifierList  {

    private String id1;
    private String id;





    private myDsl_FieldDecl mydsl_fielddecl;




    private myDsl_CommCaseLinha mydsl_commcaselinha;


    public myDsl_IdentifierList(
        String id1,        String id    ) {
        this.id1 = id1;
        this.id = id;
    }


    public String getId1() {
        return id1;
    }

    public void setId1(String id1) {
        this.id1 = id1;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public myDsl_FieldDecl getMydsl_fielddecl() {
        return mydsl_fielddecl;
    }

    public void setMydsl_fielddecl(myDsl_FieldDecl mydsl_fielddecl) {
        this.mydsl_fielddecl = mydsl_fielddecl;
    }
    public myDsl_CommCaseLinha getMydsl_commcaselinha() {
        return mydsl_commcaselinha;
    }

    public void setMydsl_commcaselinha(myDsl_CommCaseLinha mydsl_commcaselinha) {
        this.mydsl_commcaselinha = mydsl_commcaselinha;
    }

}