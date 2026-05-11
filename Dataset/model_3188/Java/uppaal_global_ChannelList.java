





import java.util.List;
import java.util.ArrayList;

public class uppaal_global_ChannelList extends ChannelPriorityItem {






    private List<IdentifierExpression> identifierexpressions;


    public uppaal_global_ChannelList(
    ) {
        super(
        );
        this.identifierexpressions = new ArrayList<>();
    }

    public uppaal_global_ChannelList(
        ArrayList<IdentifierExpression> identifierexpressions    ) {
        this.identifierexpressions = identifierexpressions;
    }


    public List<IdentifierExpression> getIdentifierexpressions() {
        return identifierexpressions;
    }

    public void addIdentifierexpression(Identifierexpression identifierexpression) {
        this.identifierexpressions.add(identifierexpression);
    }

}