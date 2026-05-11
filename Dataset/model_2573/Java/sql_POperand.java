





import java.util.List;
import java.util.ArrayList;

public class sql_POperand  {

    private String prm;





    private sql_LikeOperand sql_likeoperand;


    public sql_POperand(
        String prm    ) {
        this.prm = prm;
    }


    public String getPrm() {
        return prm;
    }

    public void setPrm(String prm) {
        this.prm = prm;
    }

    public sql_LikeOperand getSql_likeoperand() {
        return sql_likeoperand;
    }

    public void setSql_likeoperand(sql_LikeOperand sql_likeoperand) {
        this.sql_likeoperand = sql_likeoperand;
    }

}