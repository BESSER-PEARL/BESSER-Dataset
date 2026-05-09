





import java.util.List;
import java.util.ArrayList;

public class HALL_Actions_DomainPropertySet extends ActionMessageExpression {

    private String name;





    private Actions_ActionMessageExpression actions_actionmessageexpression;


    public HALL_Actions_DomainPropertySet(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Actions_ActionMessageExpression getActions_actionmessageexpression() {
        return actions_actionmessageexpression;
    }

    public void setActions_actionmessageexpression(Actions_ActionMessageExpression actions_actionmessageexpression) {
        this.actions_actionmessageexpression = actions_actionmessageexpression;
    }

}