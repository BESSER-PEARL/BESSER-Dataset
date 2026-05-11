





import java.util.List;
import java.util.ArrayList;

public class sADL_Declaration extends Expression {

    private String maxlen;
    private String len;
    private String ordinal;
    private String article;





    private List<sADL_Expression> sadl_expressions;




    private sADL_SadlTypeReference sadl_sadltypereference;


    public sADL_Declaration(
        String maxlen,        String len,        String ordinal,        String article    ) {
        super(
        );
        this.maxlen = maxlen;
        this.len = len;
        this.ordinal = ordinal;
        this.article = article;
        this.sadl_expressions = new ArrayList<>();
    }

    public sADL_Declaration(
        String maxlen,        String len,        String ordinal,        String article        ArrayList<sADL_Expression> sadl_expressions    ) {
        this.maxlen = maxlen;
        this.len = len;
        this.ordinal = ordinal;
        this.article = article;
        this.sadl_expressions = sadl_expressions;
    }

    public String getMaxlen() {
        return maxlen;
    }

    public void setMaxlen(String maxlen) {
        this.maxlen = maxlen;
    }
    public String getLen() {
        return len;
    }

    public void setLen(String len) {
        this.len = len;
    }
    public String getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(String ordinal) {
        this.ordinal = ordinal;
    }
    public String getArticle() {
        return article;
    }

    public void setArticle(String article) {
        this.article = article;
    }

    public List<sADL_Expression> getSadl_expressions() {
        return sadl_expressions;
    }

    public void addSadl_expression(Sadl_expression sadl_expression) {
        this.sadl_expressions.add(sadl_expression);
    }
    public sADL_SadlTypeReference getSadl_sadltypereference() {
        return sadl_sadltypereference;
    }

    public void setSadl_sadltypereference(sADL_SadlTypeReference sadl_sadltypereference) {
        this.sadl_sadltypereference = sadl_sadltypereference;
    }

}