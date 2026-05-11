





import java.util.List;
import java.util.ArrayList;

public class uppaal_expressions_ChannelPrefixExpression extends Expression {

    private boolean broadcast;
    private boolean urgent;





    private Type type;


    public uppaal_expressions_ChannelPrefixExpression(
        boolean broadcast,        boolean urgent    ) {
        super(
        );
        this.broadcast = broadcast;
        this.urgent = urgent;
    }


    public boolean getBroadcast() {
        return broadcast;
    }

    public void setBroadcast(boolean broadcast) {
        this.broadcast = broadcast;
    }
    public boolean getUrgent() {
        return urgent;
    }

    public void setUrgent(boolean urgent) {
        this.urgent = urgent;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

}