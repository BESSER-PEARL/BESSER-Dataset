





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_BooleanExpression extends PrimitiveExpression {

    private String body;





    private OPLmetamodel_IfExpression oplmetamodel_ifexpression;


    public OPLmetamodel_BooleanExpression(
        String body    ) {
        super(
        );
        this.body = body;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public OPLmetamodel_IfExpression getOplmetamodel_ifexpression() {
        return oplmetamodel_ifexpression;
    }

    public void setOplmetamodel_ifexpression(OPLmetamodel_IfExpression oplmetamodel_ifexpression) {
        this.oplmetamodel_ifexpression = oplmetamodel_ifexpression;
    }

}