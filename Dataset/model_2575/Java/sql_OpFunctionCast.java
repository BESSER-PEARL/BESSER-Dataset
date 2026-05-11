





import java.util.List;
import java.util.ArrayList;

public class sql_OpFunctionCast  {

    private String p;
    private String p2;
    private String type;





    private sql_LikeOperand sql_likeoperand;


    public sql_OpFunctionCast(
        String p,        String p2,        String type    ) {
        this.p = p;
        this.p2 = p2;
        this.type = type;
    }


    public String getP() {
        return p;
    }

    public void setP(String p) {
        this.p = p;
    }
    public String getP2() {
        return p2;
    }

    public void setP2(String p2) {
        this.p2 = p2;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public sql_LikeOperand getSql_likeoperand() {
        return sql_likeoperand;
    }

    public void setSql_likeoperand(sql_LikeOperand sql_likeoperand) {
        this.sql_likeoperand = sql_likeoperand;
    }

}