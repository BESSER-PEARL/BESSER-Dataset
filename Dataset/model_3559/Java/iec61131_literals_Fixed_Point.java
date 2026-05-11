





import java.util.List;
import java.util.ArrayList;

public class iec61131_literals_Fixed_Point extends Fixed_Point_Literal {

    private String valuePre;
    private String valuePost;



    public iec61131_literals_Fixed_Point(
        String valuePre,        String valuePost    ) {
        super(
        );
        this.valuePre = valuePre;
        this.valuePost = valuePost;
    }


    public String getValuepre() {
        return valuePre;
    }

    public void setValuepre(String valuePre) {
        this.valuePre = valuePre;
    }
    public String getValuepost() {
        return valuePost;
    }

    public void setValuepost(String valuePost) {
        this.valuePost = valuePost;
    }


}