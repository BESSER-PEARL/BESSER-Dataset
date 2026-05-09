





import java.util.List;
import java.util.ArrayList;

public class dsl_CastLookahead  {

    private String bitNegOp;
    private String negOp;
    private String newOp;
    private String primType;
    private String id;
    private String superOp;
    private String thisOp;
    private String openBracket;





    private dsl_Type dsl_type;




    private dsl_Type dsl_type;


    public dsl_CastLookahead(
        String bitNegOp,        String negOp,        String newOp,        String primType,        String id,        String superOp,        String thisOp,        String openBracket    ) {
        this.bitNegOp = bitNegOp;
        this.negOp = negOp;
        this.newOp = newOp;
        this.primType = primType;
        this.id = id;
        this.superOp = superOp;
        this.thisOp = thisOp;
        this.openBracket = openBracket;
    }


    public String getBitnegop() {
        return bitNegOp;
    }

    public void setBitnegop(String bitNegOp) {
        this.bitNegOp = bitNegOp;
    }
    public String getNegop() {
        return negOp;
    }

    public void setNegop(String negOp) {
        this.negOp = negOp;
    }
    public String getNewop() {
        return newOp;
    }

    public void setNewop(String newOp) {
        this.newOp = newOp;
    }
    public String getPrimtype() {
        return primType;
    }

    public void setPrimtype(String primType) {
        this.primType = primType;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSuperop() {
        return superOp;
    }

    public void setSuperop(String superOp) {
        this.superOp = superOp;
    }
    public String getThisop() {
        return thisOp;
    }

    public void setThisop(String thisOp) {
        this.thisOp = thisOp;
    }
    public String getOpenbracket() {
        return openBracket;
    }

    public void setOpenbracket(String openBracket) {
        this.openBracket = openBracket;
    }

    public dsl_Type getDsl_type() {
        return dsl_type;
    }

    public void setDsl_type(dsl_Type dsl_type) {
        this.dsl_type = dsl_type;
    }
    public dsl_Type getDsl_type() {
        return dsl_type;
    }

    public void setDsl_type(dsl_Type dsl_type) {
        this.dsl_type = dsl_type;
    }

}